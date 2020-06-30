<template>
    <v-card class="pa-3" style="text-align: left">


        <div class="d-flex justify-space-between ">
            <div class="d-flex flex-row">

                <div class="d-flex flex-column  align-center ">
                    <v-list-item-avatar
                            size="15vh" class="clickable  primary mx-1">
                        <span class="white--text display-3">{{badgeName()}}</span>
                    </v-list-item-avatar>
                    <v-card-title class="headline"><strong>{{username}}</strong></v-card-title>
                </div>
                <v-spacer class="mx-4"/>


                <div class="d-flex justify-center align-content-start flex-row flex-wrap"
                >
                    <div v-for="(item,idx) in profileData" class="d-flex align-center flex-column mx-3" :key="idx">
                        <v-card-title style="border-bottom: 1px solid black" class="text">{{getKey(idx)}}
                        </v-card-title>
                        <v-spacer class="mt-1"/>
                        <v-card-title>{{item.length}}</v-card-title>
                    </div>


                </div>


            </div>

        </div>


    </v-card>


</template>

<script>

    import store from "../../store/store";
    import router from "../../router/router";
    import _ from "lodash"

    export default {
        data() {
            return {
                values: ["followed reports", "authored reports", "followed by", "followed users"]
            }
        },
        components: {},
        methods: {

            badgeName() {
                return this.username.split(' ').map(e => e.toUpperCase()[0]).join()
            },
            goToProfile(username) {
                router.push({name: 'Profile', params: {username: username}})
            },
            getKey(idx) {

                return _.startCase(_.camelCase(idx.split('_').join()))

            }


        },

        computed: {

            username() {
                return this.$route.params.username
            },
            profileData() {
                return store.state.search.profile ? store.state.search.profile : []
            }


        }

    }
</script>
