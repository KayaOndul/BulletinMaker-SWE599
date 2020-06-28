<template>
    <div>
        <layout>


            <v-tabs class="mt-2">
                <v-tab v-if="isLoggedIn" default :to="{name:'Welcome'}">My Reports</v-tab>
                <v-tab v-if="isLoggedIn" :to="{name:'MyFollow'}">Followed Reports</v-tab>
                <v-tab :to="{name:'MyFresh'}">Fresh from Site</v-tab>
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
        data: () => ({}),
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
