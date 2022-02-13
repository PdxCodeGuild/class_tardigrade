const App = {
    data() {





        return {


            lis: [
                {
                    item: 'midori',
                    status: false

                },
                // {
                //     item: 'aoi',
                //     status: true
                // },


                // {
                //     item: 'shiro',
                //     status: false
                // },

                // {
                //     item: 'kuro',
                //     status: false
                // }





            ],
            // done :[
            //     {
            //         item:'' ,
            //         status: false

            //     }
            // ],
            

            write: '',


            still() {
                return this.lis.filter(lis => lis.completed === false)
            },

            done() {
                return this.lis.filter(lis => lis.completed === true)


            }


        }
    },



    methods: {




        add() {

            this.lis.push({
                item: this.write,
                status: false
            })

            // this.write = ''
        },


        cancel(lis) {

            // this.lis.pop(write)
            // this.delete lis[this.write]
            let index = this.lis.indexOf(lis)

            this.lis.splice(this.index, 1);
            

        },

        complete(lis) {
            // lis.style.color = 'aqua',
            lis.status = !lis.status
            // this.done.push(this.index, 1)
            // this.done.push({
            //     item: this.lis,
            //     status: true
            // })




            // toogle() {
            //     lis.status = !lis.status
            // }
            

        }




    }
}

const app = Vue.createApp(App).mount('#app')
