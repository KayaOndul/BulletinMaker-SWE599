<template>
    <div>
        <v-card
                color="grey lighten-4"
                flat

        >
            <v-toolbar>

                <v-toolbar-title @click="()=>this.$router.push({name:'Home'})"><strong
                        class="teal--text display-1 font-weight-bold">Bulletin Maker</strong></v-toolbar-title>


                <div class="d-flex flex-row justify-content-end ">

                    <v-list-item>
                        <click-icon v-if="isLoggedIn===false" :note="'Login'"
                                    :icon="'mdi-login'"
                                    :route="{name:'Login'}"/>
                        <click-icon v-else :note="'Log Out'"
                                    :icon="'mdi-logout'"
                                    :route="{name:'Logout'}"/>
                    </v-list-item>
                    <v-list-item>
                        <click-icon :note="'Register'" :icon="'mdi-account-plus'" :route="{name:'Register'}"/>
                    </v-list-item>
                    <v-list-item v-if="isLoggedIn===true">

                        <v-tooltip bottom light class="white primary--text">
                            <template v-slot:activator="{ on }">
                                <v-list-item-avatar v-on="on">
                                    <v-img :src="'https://picsum.photos/303'"/>
                                </v-list-item-avatar>
                            </template>
                            <span class=" white--text">{{username}}</span>
                        </v-tooltip>

                    </v-list-item>
                </div>


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
        <back-to-top style="display: inline-block"
                     :visibleoffset="visibleoffset"
                     :text="text"
                     :bottom="bottom"
                     :right="right"
                     :scrollFn="scrollFn"
                     @scrolled="scrolled"/>


    </div>
</template>

<script>
    import ClickIcon from "@/components/apparatus/ClickIcon";
    import NotificationsAlert from "@/components/apparatus/NotificationsAlert";
    import BackToTop from 'vue-backtotop'
    import router from "../router";
    import store from "@/store/store";
    import {mapGetters} from "vuex"

    export default {

        data() {
            return {
                showNotifications: true,
                model: '',
                isBackTopFooter: false,
                visibleoffset: 100,
                text: 'Back to top',
                bottom: '40px',
                right: '40px',
                display: 'block'
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
            // private
            this.scrollIndentBackTop = 0;
            this.scrollHeight = 0;
        },
        mounted() {

            this.scrollHeight = Math.max(
                document.body.scrollHeight, document.documentElement.scrollHeight,
                document.body.offsetHeight, document.documentElement.offsetHeight,
                document.body.clientHeight, document.documentElement.clientHeight
            ) - window.innerHeight;
            this.scrollIndentBackTop = document.body.clientHeight / 2;
        },
        watch: {
            visibleoffset(newVal) {
                document.body.style.height = (parseInt(newVal) + 2000) + 'px';
            }
        },
        methods: {

            searchItem: function () {
                router.push({path: '/Search', name: 'Search', props: true, params: {searchField: this.model}})
            },
            scrolled() {
                console.log('Scrolled !')
            },
            scrollFn: function () {
                let diff = this.scrollHeight - window.pageYOffset;
                this.isBackTopFooter = diff < (this.scrollIndentBackTop - 40 - 15);
            }
        },
        components: {BackToTop, ClickIcon,NotificationsAlert}
    }

</script>
