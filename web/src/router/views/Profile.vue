<template>


    <div>
        <layout>


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

        </layout>

    </div>


</template>

<script>
    import layout from "../layouts/layout";
    import UserCard from "@/components/User/UserCard";

    export default {
        name: 'Profile',
        data() {
            return {}
        },
        components: {UserCard, layout},
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

        }


    }
</script>


