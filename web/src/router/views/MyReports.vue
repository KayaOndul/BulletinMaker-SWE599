<template>
    <reports/>
</template>
<script>

    import Reports from "../../components/Shared/Reports";
    import store from "../../store/store";
    import reportService from "../../service/reportService";

    export default {
        name: 'MyReports',
        components: {Reports},
        data: () => ({}),

        beforeDestroy() {
            store.commit('report/resetState');
        },
        beforeRouteEnter(to, from, next) {
            const user = store.state.auth.username
            reportService.GET_ALL_REPORTS_VIA_USERNAME({user})
            next()
        },

    }

</script>
