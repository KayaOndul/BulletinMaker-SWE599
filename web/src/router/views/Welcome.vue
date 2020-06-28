<template>
    <div>
        <layout>



                <v-tabs class="mt-2">
                    <v-tab default :to="{name:'Welcome'}">My Reports</v-tab>
                    <v-tab :to="{name:'MyFollow'}">Followed Reports</v-tab>
                    <v-tab :to="{name:'MyFresh'}">Fresh from Site</v-tab>
                </v-tabs>


            <router-view></router-view>


        </layout>


    </div>

</template>

<script>

    import Layout from "../layouts/layout";

    export default {
        name: 'Welcome',
        components: {Layout},
        data: () => ({}),
        created() {

        },
        mounted() {

        },
        watch: {},
        computed: {},


        methods: {},
        beforeDestroy() {
        }
    }

</script>
