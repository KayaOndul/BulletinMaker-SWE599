<template>
    <v-container style="z-index: 3; position:absolute;right:0px">
        <v-alert class="d-flex flex-column " v-for="(alert,index) in alerts" :key="index"
                 :type="alert.includes('4')?'error':'success'"
                 mode="out-in"
                 transition="slide-x-reverse-transition"
                 dismissible
                 border="left"
                 elevation="2"
                 colored-border
                 :icon="alert.includes('4')?'mdi-close':'mdi-check'"
        >
            {{alert}}

        </v-alert>


    </v-container>
</template>

<script>
    import _ from 'lodash'
    import store from "../../store/store";


    export default {
        data() {
            return {}
        },

        computed: {


            alerts() {
                return store.state.global.alerts
            },


        },
        methods: {
            debounceRemove: _.debounce(function () {
                store.dispatch('global/removeAlert')
            }, 700)
        },
        watch: {
            alerts(newVal) {
                if (newVal.length > 0) {
                    this.debounceRemove()
                }

            }
        },

    }
</script>
