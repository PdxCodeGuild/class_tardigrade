const App = {
    //has to say data and return verbatim
    data() {
        return {
            //variable names can be pretty much anything
            hello: 'woof woof heckin woof',
            doggos: 'clifford, spike, cujo',
            cats: ['heather', 'fluffy', 'tiger', 'rex'],
            snack: '',
            selectedCat: '',
        } //closes return
    }, //closes data

    //has to say methods exactly
    //our functions go here
    methods: {
        //function names can be pretty much anything
        sayWoof() {
            console.log('sayWoof ran')
        }, //end of sayWoof

        //tree is a functional argument and can be anything you want it to be. 
        sayMeow(tree) {
            console.log(tree, 'sayMeow ran')
        }, //end of sayMeow

        snackTime() {
            this.hello = this.snack
        }

    }//end of methods

} //end of app

Vue.createApp(App).mount('#app')

