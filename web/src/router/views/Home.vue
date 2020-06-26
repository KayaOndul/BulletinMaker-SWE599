<template>
    <layout>
        <router-view></router-view>
    </layout>
</template>

<script>
    import layout from "@/router/layouts/layout";

    export default {
        name: 'Home',
        data() {
            return {
                selectedTab: 1,
                isMounted: false,
                itemsF: []
            }
        },
        components: {layout}
    }
</script>