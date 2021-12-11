import requests
import json


headers ={'accept': 'application/json'}
response = requests.get('https://icanhazdadjoke.com/', headers = headers)
print(response)

data = response.json()
print(data)










# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="utf-8">
# <meta http-equiv="X-UA-Compatible" content="IE=edge">
# <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
# <meta name="description" content="The largest collection of dad jokes on the internet" />
# <meta name="author" content="C653 Labs" />
# <meta name="keywords" content="dad,joke,funny,slack,alexa" />
# <meta property="og:site_name" content="icanhazdadjoke" />
# <meta property="og:title" content="icanhazdadjoke" />
# <meta property="og:type" content="website" />
# <meta property="og:url" content="https://icanhazdadjoke.com/j/7MZ0LR7UfFd" />
# <meta property="og:description" content="Why can't your nose be 12 inches long? Because then it'd be a foot!" />
# <meta property="og:image:url" content="https://icanhazdadjoke.com/j/7MZ0LR7UfFd.png" />
# <meta property="og:image:secure_url" content="https://icanhazdadjoke.com/j/7MZ0LR7UfFd.png" />
# <meta property="og:image:secure_url" content="https://icanhazdadjoke.com/static/smile.png" />
# <meta property="og:image:type" content="image/png" />
# <meta name="twitter:card" content="summary">
# <meta name="twitter:site" content="@icanhazdadjoke">
# <meta name="twitter:title" content="icanhzdadjoke">
# <meta name="twitter:description" content="Why can't your nose be 12 inches long? Because then it'd be a foot!">
# <meta name="twitter:image" content="https://icanhazdadjoke.com/static/smile.png">
# <meta name="twitter:url" content="https://icanhazdadjoke.com/j/7MZ0LR7UfFd" />
# <link rel="canonical" href="https://icanhazdadjoke.com/j/7MZ0LR7UfFd">
# <link rel="amphtml" href="https://icanhazdadjoke.com/j/7MZ0LR7UfFd/amp">
# <title>icanhazdadjoke</title>
# <link rel="apple-touch-icon" sizes="180x180" href="/static/apple-touch-icon.png">
# <link rel="icon" type="image/png" href="/static/favicon-32x32.png" sizes="32x32">
# <link rel="icon" type="image/png" href="/static/favicon-16x16.png" sizes="16x16">
# <link rel="manifest" href="/static/manifest.json">
# <link rel="mask-icon" href="/static/safari-pinned-tab.svg" color="#1fc8db">
# <link rel="shortcut icon" href="/static/favicon.ico">
# <meta name="msapplication-config" content="/static/browserconfig.xml">
# <meta name="theme-color" content="#ffffff">
# <meta name="slack-app-id" content="A214NCJF2">
# <link rel="stylesheet" href="/static/dist/style.css?55f4ea12">

# <script type="application/ld+json">
#       {
#     "@context": "http://schema.org",
#     "@type": "WebSite",
#     "url": "https://icanhazdadjoke.com/",
#     "name": "icanhazdadjoke",
#     "description": "The largest collection of dad jokes on the internet",
#     "potentialAction": {
#         "@type": "SearchAction",
#         "target": "https://icanhazdadjoke.com/search?term={search_term_string}",
#         "query-input": "required name=search_term_string"
#     }
# }
#     </script>
# <script type="application/ld+json">
#       {
#     "@context": "http://schema.org",
#     "@type": "Organization",
#     "url": "https://icanhazdadjoke.com/",
#     "logo": "https://icanhazdadjoke.com/static/smile.png",
#     "name": "icanhazdadjoke",
#     "description": "The largest collection of dad jokes on the internet",
#     "email": "support@icanhazdadjoke.com"
# }
#     </script>
# <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
# <script>
#       (adsbygoogle = window.adsbygoogle || []).push({google_ad_client: "ca-pub-3200991035275362", enable_page_level_ads: true
# });
#     </script>
# </head>
# <body>
# <nav class="nav has-shadow">
# <div class="container">
# <div class="nav-left">
# <a class="nav-item is-brand" href="/">
# <img src="/static/smile.svg" alt="icanhazdadjoke logo" />
# <span class="subtitle pushhalf--left">
# icanhazdadjoke
# </span>
# </a>
# </div>
# <span id="nav-toggle" class="nav-toggle">
# <span></span>
# <span></span>
# <span></span>
# </span>
# <div id="nav-menu" class="nav-right nav-menu">
# <a class="nav-item is-tab" href="/">
# <span class="icon is-small">
# <i class="fa fa-random"></i>
# </span>
# <span class="pushquarter--left">
# Random joke
# </span>
# </a>
# <a class="nav-item is-tab" href="/search">
# <span class="icon is-small">
# <i class="fa fa-search"></i>
# </span>
# <span class="pushquarter--left">
# Search jokes
# </span>
# </a>
# <a class="nav-item is-tab" href="/submit">
# <span class="icon is-small">
# <i class="fa fa-pencil-square-o"></i>
# </span>
# <span class="pushquarter--left">
# Submit new joke
# </span>
# </a>
# <div class="nav-item">
# <a href="/slack-add" style="height:40px; max-width:139px">
# <img alt="Add to Slack" height="40" width="139" src="https://platform.slack-edge.com/img/add_to_slack.png" style="width:139px; height:40px; max-height: 40px" srcset="https://platform.slack-edge.com/img/add_to_slack.png 1x, https://platform.slack-edge.com/img/add_to_slack@2x.png 2x" />
# </a>
# </div>
# <div class="nav-item">
# <a class="button" target="_blank" href="https://www.amazon.com/Brett-Langdon-icanhazdadjoke/dp/B01N6CQ3NZ/" style="background-color: #ffffff; color: #5ebfe4; border-radius: 6px; font-weight: 500; height:40px; width:139px; max-width:139px">
# <img src="/static/alexa-logo.png" style="margin-left: -0.5em;">
# Add to <strong style="margin-left: 0.25em">Alexa</strong>
# </a>
# </div>
# </div>
# </div>
# </nav>
# <section class="section">
# <div class="container">
# <div class="level">
# <div class="level-left">
# <div class="content level-item">
# <h1>Random dad joke:</h1>
# </div>
# </div>
# <div class="level-right">
# <a class="button is-primary level-item" href="/">
# <span class="icon is-small">
# <i class="fa fa-random"></i>
# </span>
# <span>
# New joke
# </span>
# </a>
# </div>
# </div>
# <div class="content">
# <div class="card">
# <div class="card-content">
# <p class="subtitle">Why can't your nose be 12 inches long? Because then it'd be a foot!</p>
# </div>
# <footer class="card-footer">
# <a class="card-footer-item" href="/j/7MZ0LR7UfFd">
# <span class="icon is-small">
# <i class="fa fa-chain"></i>
# </span>
# <span class="pushquarter--left">
# Permalink
# </span>
# </a>
# <a class="card-footer-item" target="_blank" href="https://twitter.com/intent/tweet?url=https://icanhazdadjoke.com%2Fj%2F7MZ0LR7UfFd%2Famp&text=Check+out+this+%23dadjoke&via=icanhazdadjoke">
# <span class="icon is-small">
# <i class="fa fa-twitter"></i>
# </span>
# <span class="pushquarter--left">
# Share on Twitter
# </span>
# </a>
# </footer>
# </div>
# </div>
# <div class="content pushwhole--top">
# <ins class="adsbygoogle" style="display:block" data-ad-client="ca-pub-3200991035275362" data-ad-slot="5324903139" data-ad-format="auto"></ins>
# </div>
# <script>
#           (adsbygoogle = window.adsbygoogle || []).push({});
#         </script>
# </div>
# </section>
# <footer class="footer">
# <div class="container">
# <div class="columns">
# <div class="column is-5">
# <div class="content">
# <p>
# <strong>icanhazdadjoke.com</strong> by <a href="https://c653labs.com/">C653 Labs</a>.
# </p>
# <p>
# <i>icanhazdadjoke.com</i> is the largest selection of dad jokes on the internet.
# Now supporting many different integrations to ensure you can access the dad jokes that you need wherever you are.
# </p>
# </div>
# </div>
# <div class="column is-3"></div>
# <div class="column is-2">
# <aside class="menu">
# <ul class="menu-list">
# <li><a href="/cdn-cgi/l/email-protection#4c3f393c3c233e380c252f2d22242d36282d2826232729622f2321" target="_blank">Contact</a></li>
# <li><a href="https://twitter.com/icanhazdadjoke" target="_blank">Twitter</a></li>
# <li><a href="https://slack.com/apps/A214NCJF2-icanhazdadjoke" target="_blank">Slack app</a></li>
# <li><a href="https://www.amazon.com/Brett-Langdon-icanhazdadjoke/dp/B01N6CQ3NZ/" target="_blank">Alexa skill</a></li>
# <li><a href="https://discordapp.com/api/oauth2/authorize?client_id=467365247921946626&permissions=0&scope=bot" target="_blank">Discord bot</a></li>
# <li><a href="https://marketplace.atlassian.com/plugins/com.icanhazdadjoke/cloud/overview" target="_blank">HipChat plugin</a></li>
# <li><a href="https://twistapp.com/integrations/install/20_901fa9d3df5b8784d3ddc56e" target="_blank">Twist integration</a></li>
# </ul>
# </aside>
# </div>
# <div class="column is-2">
# <aside class="menu">
# <ul class="menu-list">
# <li><a href="/about">About</a></li>
# <li><a href="/api">API</a></li>
# <li><a href="/">Random joke</a></li>
# <li><a href="/search">Search jokes</a></li>
# <li><a href="/submit">Submit new joke</a></li>
# </ul>
# </aside>
# </div>
# </div>
# </div>
# </footer>
# <script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script>
#         (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject'
#     ]=r;i[r
#     ]=i[r
#     ]||function(){
#         (i[r
#         ].q=i[r
#         ].q||[]).push(arguments)
#     },i[r
#     ].l=1*new Date();a=s.createElement(o),
#         m=s.getElementsByTagName(o)[
#         0
#     ];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
# })(window,document,'script','https: //www.google-analytics.com/analytics.js','ga');

#         ga('create', 'UA-82372853-1', 'auto');
#         ga('send', 'pageview');
#         </script>
# <script>
#       document.addEventListener('click', function (evt) {
#         if (evt.target.id === 'nav-toggle' || evt.target.parent.id === 'nav-toggle') {
#           document.getElementById('nav-menu').classList.toggle('is-active');
#     }
# });
#     </script>

# <script type="text/javascript">
#       /* <![CDATA[ */
#       var google_conversion_id = 855658655;
#       var google_conversion_language = "en";
#       var google_conversion_format = "3";
#       var google_conversion_color = "ffffff";
#       var google_conversion_label = "gdOKCMjzmHAQn6GBmAM";
#       var google_remarketing_only = false;
#       /* ]]> */
#     </script>
# <script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js"></script>
# <noscript>
#       <div style="display:inline;">
#         <img height="1" width="1" style="border-style:none;" alt="" src="//www.googleadservices.com/pagead/conversion/855658655/?label=gdOKCMjzmHAQn6GBmAM&amp;guid=ON&amp;script=0"/>
#       </div>
#     </noscript>
# </body>
# </html>