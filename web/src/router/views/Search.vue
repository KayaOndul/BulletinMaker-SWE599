<template>

    <div>
        <layout>
            <v-card class="my-4"

                    color="primary"
                    dark
            >
                <div class="d-flex flex-no-wrap justify-space-between ">
                    <v-card-title class="headline">Searching for : <strong> {{` ${queryParam}`}} </strong>
                    </v-card-title>


                </div>

            </v-card>
            <v-data-table
                    :headers="headers"
                    :items="searchFeed"
                    item-key="id+name+category"
                    class="elevation-1"
                    disable-pagination
                    @click:row="clickHandler"
                    style="cursor: pointer"

            >

            </v-data-table>
        </layout>
    </div>


</template>

<script>

    import layout from '../layouts/layout'
    import {mapGetters} from 'vuex'
    import searchService from "../../service/searchService";
    import router from "../router";

    export default {
        components: {layout},
        name: 'Search',
        data() {
            return {
                headers: [
                    {
                        text: 'Search item',
                        align: 'start',
                        value: 'name',
                    },
                    {text: 'Owner', value: 'owner'},
                    {text: 'Category', value: 'category'},
                ],


            }
        },

        computed: {
            ...mapGetters({
                searchFeed: 'search/searchFeed',
            }),

            queryParam() {
                return this.$route.params.searchparam ? this.$route.params.searchparam : ''
            },


        },

        watch: {
            queryParam: {
                immediate: false,
                handler(newVal) {
                    if (newVal) {
                        const payload = {'keyword': newVal}
                        searchService.SEARCH(payload)
                    }
                }
            },

        },

        beforeRouteEnter(to, from, next) {
            // const keyword = this.$route.params.searchparam
            const keyword = to.params.searchparam
            searchService.SEARCH({keyword})
                .then(() => next())
        },

        methods: {


            clickHandler(item) {
                if(item.component==='Profile'){
                    router.push({name:'Profile',params:{
                            username:item.name
                        }})
                }
                else if (item.component==='Report'){
                    router.push({name:'report',params:{
                            id:item.id
                        }})
                }
            }


        }
    }
</script>

