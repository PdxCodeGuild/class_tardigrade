const App = {
    data() {





        return {

            lis: 'midori, aoi,shiro,kuro',

            write: '',


        }
    },



    methods: {




        add() {




            let form = document.querySelector('#form')


            this.lis.push(this.write)
            console.log()
        },


        cancel() {

            this.lis.remove(this.write)
            console.log(lis)
        },

        complete() {
            console.log(lis)
        }

    }



}


Vue.createApp(App).mount('#app')
