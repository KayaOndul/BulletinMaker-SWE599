<template>
    <v-card class="pa-3" style="text-align: left">


        <div class="d-flex justify-start align-center ">




        </div>

        <div class="d-flex justify-space-between ">
            <div class="d-flex flex-column">

                <div class="d-flex flex-row  align-center ">
                    <v-img width="150" style="border-radius: 50%"
                           :src="'https://picsum.photos/302'">

                    </v-img>

                    <div class="d-flex justify-end flex-column">
                        <v-card-title><strong>{{this.userNameHandler()}}</strong></v-card-title>
                        <v-card-subtitle><strong>User Since::</strong>{{changeTime(items.date_joined)}}</v-card-subtitle>
                    </div>
                </div>


            </div>


        </div>


    </v-card>


</template>

<script>
    import moment from 'moment'
    import store from "../../store/store";
    import {mapGetters} from 'vuex';

    export default {
        data() {
            return {}
        },
        components: {},
        methods: {

            changeTime(time) {
                return moment(time)
            }, userNameHandler() {
                return store.state.auth.username ? store.state.auth.username : ''
            }

        },

        computed: {
            ...mapGetters('auth', ['isLoggedIn']),

            showActions() {

                if (localStorage.getItem('username') === this.$route.params.username) {
                    return true
                }
                return false
            },

            items() {
                return store.state.global.visitedUserDetails ? store.state.global.visitedUserDetails : []
            }
        }

    }
</script>
