<template>
    <div>
        <v-card
                color="grey lighten-4"
                flat

        >
            <v-toolbar>


                <v-toolbar-title style="cursor: pointer" @click="goHome"
                                 class="teal--text display-1  mr-3 font-weight-bold">Bulletin Maker
                </v-toolbar-title>
                <v-list-item style="max-width: 50%">
                    <v-text-field
                            label="Search in Site For Users and Reports "
                            class=" mt-6"
                            @keypress.enter.prevent="searchItem"
                            v-model="model"
                            outlined
                            rounded
                            :color="'teal darken-4'"
                            :background-color="'grey lighten-5'"
                            flat
                            clearable
                            dense
                            light
                    ></v-text-field>
                </v-list-item>
                <v-spacer/>

                <v-spacer/>
                <v-list-item-group v-if="this.isLoggedIn===false" class="d-flex flex-row">
                    <v-list-item>
                        <click-icon :note="'Register'" :icon="'mdi-account-plus'" :route="{name:'Register'}"/>

                    </v-list-item>
                    <v-list-item>
                        <click-icon :note="'Login'"
                                    :icon="'mdi-login'"
                                    :route="{name:'Login'}"/>

                    </v-list-item>

                </v-list-item-group>
                <v-list-item-group v-if="isLoggedIn===true" class="d-flex flex-row justify-end">


                    <v-list-item>


                        <click-icon :note="'Create New Report'"
                                    :icon="'mdi-plus'"
                        />
                    </v-list-item>


                    <v-list-item>
                        <click-icon :note="'Dashboard'"
                                    :icon="'mdi-home'"
                                    :route="{name:'Profile'}"/>

                    </v-list-item>

                    <v-list-item>

                        <click-icon :note="'Log Out'"
                                    :icon="'mdi-logout'"
                                    :route="{name:'MyFresh'}"/>

                    </v-list-item>
                    <v-list-item>

                        <v-tooltip top light class="  primary--text">
                            <template v-slot:activator="{ on }">

                                <v-list-item-avatar v-on="on" @click="routeHandler()"
                                              size="5vh"  class="clickable  primary mx-1">
                                   <span class="white--text headline">{{username.toUpperCase()[0]}}</span>
                                </v-list-item-avatar>
                            </template>
                            <span class=" white--text">{{username}}</span>
                        </v-tooltip>

                    </v-list-item>
                </v-list-item-group>


            </v-toolbar>
        </v-card>


        <notifications-alert/>
        <v-overlay :value="this.loading">
            <v-progress-circular
                    :size="100"
                    color="blue"
                    indeterminate
            ></v-progress-circular>
        </v-overlay>
        <slot/>
        <go-top class="primary accent-text"	/>



    </div>
</template>

<script>
    import ClickIcon from "@/components/apparatus/ClickIcon";


    import NotificationsAlert from "@/components/apparatus/NotificationsAlert";
    import GoTop from '@inotom/vue-go-top'
    import router from "../router";
    import store from "@/store/store";
    import {mapGetters} from "vuex"

    export default {

        data() {
            return {

                model: '',

            }
        },

        computed: {
            ...mapGetters({
                isLoggedIn: 'auth/isLoggedIn',
                username: 'auth/username'
            }),

            loading() {
                return store.state.global.loading
            },
        },
        created() {

        },
        mounted() {

        },
        watch: {

        },
        methods: {
            routeHandler() {
                const username=store.state.auth.username
                router.push({name: 'Profile',params:{username:username}})
            },
            searchItem: function () {
                router.push({path: '/Search', name: 'Search', props: true, params: {searchField: this.model}})
            },

            goHome() {
                router.push({name: 'MyFresh'})
            }
        },
        components: { ClickIcon, NotificationsAlert,GoTop}
    }

</script>

