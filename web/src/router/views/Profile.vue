<template>


    <div>
        <layout>


            <Header :name="'Profile'"/>
            <UserCard/>
            <v-spacer class="pa-3"/>
            <v-tabs v-model="tabs" class="mt-2">
                <v-tab :to="{name:'UserReports'}">Authored Reports</v-tab>
                <v-tab :to="{name:'UserFollow'}">Followed Reports</v-tab>
                <v-tab :to="{name:'Friends'}">Friends</v-tab>

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
            return {
                tabs: null
            }
        },
        components: {Header, UserCard, layout},
        watch: {
            $route(newVal, oldVal) {
                if (newVal.params.username != oldVal.params.username) {
                    const username = newVal.params.username
                    reportService.GET_ALL_REPORTS_VIA_USERNAME({user: username})
                }

            }
        },

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


