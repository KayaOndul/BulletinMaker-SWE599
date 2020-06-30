<template>


    <div>
        <layout>


            <Header :name="'Profile'"/>
            <UserCard/>
            <v-spacer class="pa-3"/>
            <v-tabs class="mt-2">
                <v-tab default :to="{name:'UserReports'}">Authored Reports</v-tab>
                <v-tab :to="{name:'UserFollow'}">Followed Reports</v-tab>

            </v-tabs>


            <router-view></router-view>


        </layout>

    </div>


</template>

<script>
    import layout from "../layouts/layout";
    import UserCard from "@/components/User/UserCard";
    import Header from "../../components/Header";
    import store from "../../store/store";
    import profileService from "../../service/profileService";
    import reportService from "../../service/reportService";

    export default {
        name: 'Profile',
        data() {
            return {}
        },
        components: {Header, UserCard, layout},
        computed: {},

        watch: {
            $route() {
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
            store.commit('report/resetState')

        },
        beforeRouteEnter(to, from, next) {
            const username = to.params.username
            reportService.GET_ALL_REPORTS_VIA_USERNAME({user: username})
                .then(() => profileService.GET_PROFILE({username})
                )
                .then(() => next())


        }


    }
</script>


