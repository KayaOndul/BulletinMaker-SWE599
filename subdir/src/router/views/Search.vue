<template>

    <div>

        <v-card class="my-4"

                color="primary"
                dark
        >
            <div class="d-flex flex-no-wrap justify-space-between ">
                <v-card-title class="headline">Searching for : <strong>{{' '+replacehyphen(queryParam)}}</strong>
                </v-card-title>


            </div>

        </v-card>
        <v-data-table
                :headers="headers"
                :items="searchResponse"
                item-key="id+name+category"
                class="elevation-1"
                disable-pagination
                @click:row="clickHandler"
                style="cursor: pointer"

        >

        </v-data-table>

    </div>


</template>

<script>

    import store from "../../store/store";
    import searchService from "../../service/searchService";
    import mockSearch from "../../mocks/mockSearch"

    export default {
        name: 'Search',
        data() {
            return {
                headers: [
                    {
                        text: 'Search item',
                        align: 'start',
                        value: 'name',
                    },
                    {text: 'Category', value: 'category'},
                ],
                items: []

            }
        },

        computed: {
            queryParam() {
                return this.$route.query.searchField ? this.$route.query.searchField : []
            },

            searchResponse() {
                let retVal = store.state.global.searchResponse ? store.state.global.searchResponse : []
                console.log(retVal)
                return mockSearch


            }
        },

        watch: {

            queryParam: {
                immediate: true,
                handler(newVal) {
                    if (newVal) {
                        console.log(newVal)
                        searchService.SEARCH(newVal)
                    }
                }
            }

        },


        methods: {
            replacehyphen(val) {
                if (val && val.includes('-')) {
                    return val.replaceAll('-', ' ')
                }
                return val

            },

            clickHandler(item) {
                console.log(item)

                this.$router.push({name: item.component, params: {name: item.name}})
            }


        }
    }
</script>

