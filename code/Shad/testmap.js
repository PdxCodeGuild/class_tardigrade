import QtQuick 2.9
import QtQuick.Controls 2.2
import QtQuick.Controls.Material 2.2

import ArcGIS.AppFramework 1.0

import ArcGIS.AppFramework.Authentication 1.0
import ArcGIS.AppFramework.WebView 1.0
import ArcGIS.AppFramework.Platform 1.0
import Esri.ArcGISRuntime 100.10

import "Assets" as Assets
import "Controls" as Controls
import "Widgets" as Widgets
import "./Views/Controller"

App {
    id: app

    width: 421
    height: 725

    Material.background: colors.view_background

    LayoutMirroring.enabled: appManager.isRTL
    LayoutMirroring.childrenInherit: appManager.isRTL

    // Reference

    // parameters for integration with apps where embedded = false
    property bool isAddLayerMode:false
    property var refreshToken:""
    property var userName:""
    property var userpassword:""
    property var basemapUrl:""
    property var token:""
    property bool isEmbedded:true
    property var layerType:""
    property string layerUrl:""
    property bool isPrivateItem:false
    property string appTitle:""
    property string itemId:""
    property url portalUrl:""
    property Portal securedPortal:null


    property alias colors: colors
    property alias constants: constants
    property alias strings: strings
    property alias fonts: fonts
    property alias images: images
    property alias components: components
    property alias appManager: appManager
    property alias locationManager: locationManager
    property alias credentialManager: credentialManager
    property alias secureStorageManager: secureStorageManager
    property alias dataServiceManager: dataServiceManager
    property alias scriptManager: scriptManager
    property alias mspkUtility: mspkUtility
    property alias dialog: dialog
    property alias browserView: browserView
    readonly property real scaleFactor: AppFramework.displayScaleFactor
    readonly property real baseUnit: app.units(8)
    readonly property real headerHeight: 7 * app.baseUnit
    readonly property real defaultMargin: 2 * app.baseUnit
    readonly property real iconSize: 5 * app.baseUnit
    property string clientId:""
    property var portal: null

    property bool isAppInactive: false
    property bool isBackButtonPressed: false
    property bool isAppInitialized: false
    property AuthenticationController controller: AuthenticationController {}

    property int portalType:0

    signal updateListModels()

    Keys.onPressed: {
        if (event.key === Qt.Key_Back || event.key === Qt.Key_Escape) {
            isBackButtonPressed = true;

            event.accepted = true;
        }
    }

    Keys.onReleased: {
        if (event.key === Qt.Key_Back || event.key === Qt.Key_Escape) {
            if (isBackButtonPressed) {
                if (dialog.opened)
                    dialog.close();
                else if (typeof stackView.currentItem.backButtonPressed === "function")
                    stackView.currentItem.backButtonPressed();

                isBackButtonPressed = false;
                event.accepted = true;
            }
        }
    }

    // Model
    ListModel {
        id: onlineModel
    }

    ListModel {
        id: mspkCloudModel
    }

    // Assets
    Assets.Colors { id: colors }
    Assets.Strings { id: strings }
    Assets.Fonts { id: fonts }
    Assets.Images { id: images }
    Assets.Components { id: components }
    Assets.Constants { id: constants }

    // Controls
    Controls.AppManager {
        id: appManager

        onIsOnlineChanged: {
            if (isOnline) {
                if (isAppInitialized)
                    updateListModels();
            } else {
                if (dataServiceManager.isBusy)
                    dataServiceManager.stopService();

                toastMessage.show(strings.network_out);
            }
        }

        onAppStateChanged: {
            if (Qt.platform.os === "ios" || Qt.platform.os === "android") {
                if (appState === Qt.ApplicationActive) {
                    if (isAppInactive) {
                        isAppInactive = false;

                        dataServiceManager.stopService();
                    }

                    if (credentialManager.signedIn)
                        credentialManager.renew(() => {}, () => {
                                                    signOut();
                                                });
                }

                if (appState === Qt.ApplicationSuspended)
                    isAppInactive = true;
            }
        }
    }

    // Network manager
    Controls.NetworkManager {
        id: networkManager
    }

    Controls.ArcGISRuntimeHelper {
        id: arcGISRuntimeHelper
    }

    Controls.LocationManager {
        id: locationManager
    }

    Controls.CredentialManager {
        id: credentialManager

        settings: app.settings
        secureStorageManager: app.secureStorageManager

        onFailedToRenew: {
            signOut();
        }
    }

    Controls.SecureStorageManager {
        id: secureStorageManager
    }

    Controls.DataServiceManager {
        id: dataServiceManager

        rootUrl: portal ? portal.url + "/sharing/rest" : ""
        token: portal && portal.credential? portal.credential.token : ""
    }

    Controls.ScriptManager {
        id: scriptManager
    }

    Controls.MSPKUtility {
        id: mspkUtility
    }

    StackView {
        id: stackView

        anchors.fill: parent
        initialItem: components.landingPageComponent
    }

    Widgets.ToastMessage {
        id: toastMessage
    }

    Widgets.Dialog {
        id: dialog
    }

    BrowserView {
        id: browserView

        primaryColor: appManager.appSchema.brandColor
        foregroundColor: appManager.appSchema.brandTextColor
    }
    PortalQueryParametersForItems {
        id: queryParameters
        types: {
            return [ Enums.PortalItemTypeWebScene ]
        }
        searchString: app.itemId
        sortOrder: Enums.PortalQuerySortOrderDescending
        sortField: "modified"
        limit: 1
    }

    Component.onCompleted: {
        appManager.initialize();

        setStatusBar();

        isAppInitialized = true;

        if(appManager.isOnline && !isEmbedded)
        {
            ArcGISRuntimeEnvironment.setLicense("runtimelite,1000,rud6166262739,none,S080TK8EL9E5003AD113")
            loadSecuredPortal()
        }
        else
        {
            initialize();
        }
    }


    function loadSecuredPortal (callback) {
        //console.log("loading secured portal")
        var _credential
        if(!app.securedPortal)
        {
            if(app.refreshToken === "")
            {

                var pwcredentialInfo = {
                    password:app.userpassword,
                    token:app.token,
                    username:app.userName,

                }
                _credential = arcGISRuntimeHelper.createAndReturnCredential(app.clientId, pwcredentialInfo, app.portalUrl)

            }
            else
            {                
                var _credentialInfo = {
                    oAuthRefreshToken:app.refreshToken,
                    token: app.token
                }
                _credential = arcGISRuntimeHelper.createAndReturnCredential(app.clientId, _credentialInfo, app.portalUrl)


            }



             var _portal = arcGISRuntimeHelper.createAndReturnPortal(

                        app.clientId, app.portalUrl, _credential, function() {
                            portal = _portal;
                            securedPortal = portal

                            if(app.itemId > "")
                            {
                                //portal = _portal;
                                portal.onFindItemsStatusChanged.connect(openApp);
                                portal.findItems(queryParameters)
                            }

                        }, function() {

                            console.log("failed to load")
                            let errorMessage = portal.error.message
                            if(portal.error.code === 25)
                            {
                                let _extendedErrorType = portal.error.extendedErrorType
                                switch(_extendedErrorType){
                                case 0:
                                    if(errorMessage > "")
                                        errorMessage += ":" + strings.network_error
                                    else
                                        errorMessage += strings.network_error
                                    break;
                                case 1:
                                    if(errorMessage > "")
                                        errorMessage += ":" + strings.file_io_error
                                    else
                                        errorMessage += strings.file_io_error
                                    break;
                                case -1:
                                    if(errorMessage > "")
                                        errorMessage += ":" + strings.failed_to_load
                                    else
                                        errorMessage += strings.failed_to_load



                                }
                            }
                            if(!errorMessage > "")
                                errorMessage = strings.failed_to_load

                            displayDialog(strings.error, errorMessage, strings.okay, "", false, false, function() {
                                dialog.close();
                                if(app.parent)
                                    app.parent.exitApp()
                            }, function() {})

                        });

            _portal.load();

        }
        else
        {
            app.securedPortal.onFindItemsStatusChanged.connect(openApp);
            app.securedPortal.findItems(queryParameters)

        }

    }


    function openApp()
    {
        if(app.securedPortal){
            if (app.securedPortal.findItemsStatus === Enums.TaskStatusCompleted)
            {
                var infoPage = components.infoPageComponent.createObject(
                            null, {
                                param: {itemId:app.itemId,itemTitle:app.appTitle},
                                isMSPK: false
                            });
                infoPage.onNeedsDialog.connect((addMsg)=>{
                                                   displayDialog(strings.error, addMsg, strings.okay, "", false, false, function() {
                                                       dialog.close();
                                                   }, function() {});

                                               })
                stackView.push(infoPage)

            }
        }
    }


    function initialize() {
        credentialManager.attemptAutoSignIn(
                    () => {
                        navigateToHomePage();
                    }, () => {
                        if (!appManager.isOnline && appManager.appSchema.isSignInRequired) {
                            displayOfflineDialog();
                        } else {
                            credentialManager.clear();
                            clearAppSettings();

                        }
                    });
    }


    //

    function addLayerToMap()
    {
        if(app.layerType === "Vector Tile Service")
        {
            let  _sceneProperties = {"fileUrl": "","isMapArea":false,"mapId":"","layerUrl":layerUrl}

            var infoPage = components.infoPageComponent.createObject(
                        null, {
                            // param: listModel.get(index),
                            //isMSPK: isMSPK
                        });



            stackView.push(infoPage);


        }
        else
        {
            addFeatureService(parseFeatureServiceResponse)

        }
    }

    function parseFeatureServiceResponse(response)
    {

        var serviceObj = JSON.parse(response)
        if(serviceObj.error)
        {
            let error = serviceObj.error.message
            if(serviceObj.error.code === 499) //need token
            {
                addFeatureService(parseFeatureServiceResponse,true)
            }
            else
            {

                app.messageDialog.show(qsTr("Error"),error)

                app.messageDialog.connectToAccepted(function () {
                    app.parent.exitApp()
                })
            }

        }
        else
        {
            var layers = serviceObj.layers
            let  mapProperties = {"fileUrl": "","mapId":"","layerUrl":layerUrl,"layers":layers}

            var infoPage = components.infoPageComponent.createObject(
                        null, {
                            // param: listModel.get(index),
                            //isMSPK: isMSPK
                        });


            stackView.push(infoPage, {destroyOnPop: true, "mapProperties": mapProperties, "portalItem": ""})
        }


    }

    function addFeatureService (callback,tokenReqd) {
        //get the json from the featureServiceUrl
        if(!tokenReqd)
            tokenReqd = false
        var component = selfnetworkRequestComponent;
        var networkRequest = component.createObject(parent);
        networkRequest.url = layerUrl
        networkRequest.callback = callback
        var obj = {
            "f": "json",

        }

        if((app.isPrivateItem) || tokenReqd)
        {
            obj = {
                "f": "json",
                "token":token

            }
        }

        networkRequest.send(obj)

    }



    Component{
        id: selfnetworkRequestComponent
        NetworkRequest{
            id: networkRequest

            property var name;
            property var callback;
            followRedirects: true
            ignoreSslErrors: true
            method: "GET"

            responseType: "json"



            onReadyStateChanged: {
                if (readyState === NetworkRequest.DONE ){
                    if(errorCode != 0){
                        //fileFolder.removeFile(networkRequest.name);
                        //loadStatus = 2;

                    } else {

                        if (callback) {
                            callback(responseText);
                        }
                    }
                }
            }

            function getFeatureServiceJson(serviceUrl,callback){


                networkRequest.url = serviceUrl;
                //networkRequest.responsePath = mapAreaThumbnailFolder.path + "/" + downloadedmapareaId + "_thumbnail" + "/" + thumbnailImgName;
                networkRequest.callback = callback;
                networkRequest.send();

            }
        }
    }






    //

    function searchApp()
    {
        if (portal.findItemsStatus === Enums.TaskStatusCompleted)
        {
            var _findItemResult = portal.findItemsResult;
            if(_findItemResult.itemResults.count > 0)
                signInPublicPortal()
        }
    }

    function setStatusBar() {
        if (StatusBar.supported) {
            StatusBar.visible = true;

            if (appManager.isLightBrandColor)
                StatusBar.theme = StatusBar.Light;
            else
                StatusBar.theme = StatusBar.Dark;

            if (appManager.isiOS)
                StatusBar.color = "transparent";

            if (appManager.isAndroid)
                StatusBar.color = appManager.appSchema.brandColor;
        }
    }

    function signInPublicPortal() {
        if (appManager.isOnline) {
            console.log("signInPublicPortal");

            var _portal = arcGISRuntimeHelper.createAndReturnPortal(
                        "", appManager.appSchema.portalUrl, null, function() {

                            if(portalType === 2 || portalType === 3) { //portal type is IWA or PKI
                                navigateToSignInPage();
                            }
                            else{
                                portal = _portal;
                                if(app.isEmbedded)
                                    navigateToHomePage();
                                else
                                {
                                    var infoPage = components.infoPageComponent.createObject(
                                                null, {
                                                    param: {itemId:app.itemId},
                                                    isMSPK: false
                                                });
                                    stackView.push(infoPage)
                                }
                            }

                        }, () => {
                            if(portalType === 2 || portalType === 3) { //portal type is IWA or PKI
                                navigateToSignInPage();
                            }
                            else{
                                displayDialog(strings.error, strings.unable_to_access_portal, strings.okay, "", false, false, () => {
                                                  dialog.close();
                                              }, () => {
                                                  dialog.close();
                                              })
                                credentialManager.clear();
                                clearModelData();
                                clearAppSettings();
                                portalType = 0;
                            }

                        });
            _portal.load();
        } else {
            navigateToHomePage();
        }
    }

    function signOut() {
        credentialManager.clear();
        clearModelData();
        clearAppSettings();
        portalType = 0;

        if (appManager.appSchema.isSignInRequired)
            navigateView("landingPage");
        else{
            signInPublicPortal();
        }
    }

    function clearModelData() {
        onlineModel.clear();
        mspkCloudModel.clear();
    }

    function clearAppSettings() {
        if (portal)
            portal.cancelLoad();

        portal = null;
    }

    function displayDialog(title, message, acceptText, rejectText, isAcceptHighlighted, isRejectHighlighted, accept, reject) {
        dialog.display(title,
                       message,
                       acceptText,
                       rejectText,
                       isAcceptHighlighted,
                       isRejectHighlighted,
                       function() {
                           accept();
                       },
                       function() {
                           reject();
                       });
    }

    function navigateView(pageName) {
        stackView.pop(stackView.find(function(page) {
            return page.objectName === pageName;
        }));
    }

    function navigateToHomePage() {
        var _homePage;

        _homePage = stackView.find(function(page) {
            return page.objectName === "homePage";
        })

        if (!_homePage) {
            _homePage = components.homePageComponent.createObject(null);

            _homePage.connectPortalEventHandlers();

            stackView.push(_homePage);
        } else {
            navigateView("homePage");

            _homePage.connectPortalEventHandlers();


            _homePage.refresh();
        }
    }

    function navigateToSignInPage() {
     controller.cancelChallenge()
        var _signInPage = components.signInPageComponent.createObject(
                    null, {
                        portalUrl: appManager.appSchema.portalUrl,
                        clientId: appManager.appSchema.clientId
                    });

        _signInPage.onSucceed.connect(function() {
            clearModelData();

            credentialManager.save();

            navigateToHomePage();
        })

        //Successfully navigated to sign in page means the internet is connected
        //and the portal type is known
        //if the sign in page is still failed to load that means the portal is not accessible using this internet
        _signInPage.onFailed.connect(function(){
            displayDialog(strings.error, strings.unable_to_access_portal, strings.okay, "", false, false, () => {
                              dialog.close();
                              stackView.pop();
                          }, () => {
                              dialog.close();
                              stackView.pop();
                          })
            credentialManager.clear();
            clearModelData();
            clearAppSettings();
            portalType = 0;
        });

        _signInPage.onBack.connect(function() {
            stackView.pop();
        });

        stackView.push(_signInPage);
    }

    function displayOfflineDialog() {
        displayDialog("",
                      strings.network_out,
                      strings.okay,
                      "",
                      false,
                      false,
                      function() {
                          dialog.close();
                      },
                      function() {
                          dialog.close();
                      });
    }

    function isFieldVisible(fields,fieldName)
    {
        for(var k=0;k< fields.length; k++)
        {
            var field = fields[k]
            var name = ""
            if(field.name)
                name = field.name
            else if(field.fieldName)
                name = field.fieldName


            if(name.toUpperCase() === fieldName.toUpperCase())
            {
                if(field.visible)
                    return field.visible
                else
                    return true

            }
        }
        return true
    }

    function getFieldAlias(fields,fieldName)
    {
        for(var k=0;k< fields.length; k++)
        {
            var field = fields[k]
            var name = ""
            if(field.name)
                name = field.name
            else if(field.fieldName)
                name = field.fieldName


            if(name.toUpperCase() === fieldName.toUpperCase())
            {
                if(field.label)
                    return field.label
                else
                    return field.alias

            }
        }
        return fieldName
    }


    function getCodedValue(fields,fieldName,fieldValue)
    {
        for(var k=0;k< fields.length; k++)
        {
            var field = fields[k]
            if(field.name === fieldName)
            {
                var domain = field.domain
                if(domain && domain.codedValues)
                {
                    var codedValues = domain.codedValues

                    for(var x=0;x<codedValues.length;x++)
                    {
                        if(codedValues[x].code  ===  fieldValue)
                        {
                            var codedValueObj = codedValues[x]
                            return codedValueObj.name
                        }
                    }
                }
                else
                    return fieldValue

            }
        }
        return fieldValue
    }

    function getFormattedFieldValue(_fieldVal)
    {


        var isNotNumber = isNaN(_fieldVal)
        if(_fieldVal && !isNotNumber)
        {
            var formattedVal = _fieldVal.toLocaleString()
            if(formattedVal)
                _fieldVal = formattedVal
        }
        //check if it is a date
        var dt = Date.parse(_fieldVal)
        if(dt)
        {
            var date_ob = new Date(dt)
            // year as 4 digits (YYYY)
            var year = date_ob.getFullYear()
            // month as 2 digits (MM)
            var month = ("0" + (date_ob.getMonth() + 1)).slice(-2);
            // date as 2 digits (DD)
            var day = ("0" + date_ob.getDate()).slice(-2);
            var formattedDateVal= month + "/"+ day + "/" + year

            _fieldVal = formattedDateVal

        }
        return _fieldVal
    }

    function units (num) {
        return num ? num * AppFramework.displayScaleFactor : num
    }
}