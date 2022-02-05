const App = {
    data() {
        return {
            randomRecipeInstructions: '',
        }
    },

    created() {
        this.getRandomRecipe()
    },

    methods: {
        getRandomRecipe() {
            axios({
                method: 'get',
                url: 'https://api.spoonacular.com/recipes/random',
                headers: {Accept: 'application/json'},
                params: {apiKey:'c0706aec64ba455eb06753d6e855a6e5' }
            })
            .then(response => {
                console.log(response.data.recipes)
                this.randomRecipeInstructions = response.data.recipes[0].instructions
            })
        }
    }

}

Vue.createApp(App).mount('#app')
