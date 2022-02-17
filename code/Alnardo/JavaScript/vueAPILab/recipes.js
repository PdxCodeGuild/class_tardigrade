const App = {
    data() {
        return {
            randomRecipeInstructions: '',
            randomRecipePhoto: '',
            randomRecipeTitle: '',
            randomRecipeSummary: '',
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
                this.randomRecipePhoto = response.data.recipes[0].image
                this.randomRecipeTitle = response.data.recipes[0].title
                this.randomRecipeSummary = response.data.recipes[0].summary
            })
        }
    }

}

Vue.createApp(App).mount('#app')
