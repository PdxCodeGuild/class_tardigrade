const App = {
    data() {





        return {

            lis:'midori, aoi,shiro,kuro',
            
            write: '',


        }
    },



    methods: {




        add() {




            let form = document.querySelector('#form')


            let p= lis.push(user)
            console.log(p)
        },


        cancel() {

            lis.push('input')
            console.log(lis)
        },

        complete() {
            console.log(lis)
        }

    }



}


Vue.createApp(App).mount('#app')
