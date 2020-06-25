<template>


            <div >
                <v-card class="my-4"

                        color="primary"
                        dark
                >
                    <div class="d-flex flex-no-wrap justify-space-between ">
                        <v-card-title class="headline">Profile</v-card-title>


                    </div>

                </v-card>
                <UserCard/>
                <v-spacer class="pa-3"/>
                <div class="d-flex justify-space-between mb-12">
                </div>
                <v-spacer class="pa-3"/>
                <div class="d-flex justify-space-between">
                    <UserFollowedUsers/>
                </div>
                <v-spacer class="pa-3"/>
                <div class="d-flex justify-space-between">
                </div>
                <v-spacer class="pa-3"/>
                <div class="d-flex justify-space-between">
                </div>
                <v-spacer class="pa-3"/>
                <div class="d-flex justify-space-between">
                </div>
                <v-spacer class="pa-3"/>


            </div>



</template>

<script>

    import store from "../../store/store";
    import UserCard from "@/components/User/UserCard";
    import UserFollowedUsers from "@/components/User/UserFollowedUsers";
    export default {
        name: 'Profile',
        data() {
            return {

            }
        },
        components: { UserCard, UserFollowedUsers},
        computed: {},

        watch: {
            $route(){
                this.getUserDetails()
            }
        },


        mounted() {
            this.getUserDetails()

        },
        methods: {
            getUserDetails() {




            }
        }
        ,
        beforeDestroy() {
            store.commit('wiki/reset')
            store.commit('postStore/resetState')
            store.commit('postTypeStore/resetState')
            store.commit('communityStore/resetState')
        }


    }
</script>


