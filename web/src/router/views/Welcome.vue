<template>
    <div>
        <layout>


            <v-tabs v-model=tabs  class="mt-2">
                 <v-tab :to="{name:'MyFresh'}">Fresh from Site</v-tab>
                <v-tab v-if="isLoggedIn" default :to="{name:'MyReport'}">My Reports</v-tab>
                <v-tab v-if="isLoggedIn" :to="{name:'MyFollow'}">Followed Reports</v-tab>

            </v-tabs>


            <router-view></router-view>


        </layout>


    </div>

</template>

<script>

    import Layout from "../layouts/layout";
    import {mapGetters} from 'vuex'

    export default {
        name: 'Welcome',
        components: {Layout},
        data: () => ({
            tabs:null
        }),
        created() {

        },
        mounted() {

        },
        watch: {},
        computed: {
            ...mapGetters('auth', ['isLoggedIn']),
        },


        methods: {},
        beforeDestroy() {
        }
    }

</script>
