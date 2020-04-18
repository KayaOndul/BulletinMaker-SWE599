<template>
    <div>
        <v-card
                color="grey lighten-4"
                flat

        >
            <v-toolbar>


                <v-toolbar-title><strong  class="teal--text display-1 font-weight-bold" >Bulletin Maker</strong></v-toolbar-title>






            </v-toolbar>
        </v-card>

        <slot/>
        <back-to-top style="display: inline-block"
                     :visibleoffset="visibleoffset"
                     :text="text"
                     :bottom="bottom"
                     :right="right"
                     :scrollFn="scrollFn"
                     @scrolled="scrolled"/>


    </div>
</template>

<script>

    import BackToTop from 'vue-backtotop'
    import router from "../router";

    export default {

        data() {
            return {
                showNotifications: true,
                model: '',
                isBackTopFooter: false,
                visibleoffset: 100,
                text: 'Back to top',
                bottom: '40px',
                right: '40px',
                display: 'block'
            }
        },
        created() {
            // private
            this.scrollIndentBackTop = 0;
            this.scrollHeight = 0;
        },
        mounted() {

            this.scrollHeight = Math.max(
                document.body.scrollHeight, document.documentElement.scrollHeight,
                document.body.offsetHeight, document.documentElement.offsetHeight,
                document.body.clientHeight, document.documentElement.clientHeight
            ) - window.innerHeight;
            this.scrollIndentBackTop = document.body.clientHeight / 2;
        },
        watch: {
            visibleoffset(newVal) {
                document.body.style.height = (parseInt(newVal) + 2000) + 'px';
            }
        },
        methods: {

            searchItem: function () {
                router.push({path: '/Search', name: 'Search', props: true, params: {searchField: this.model}})
            },
            scrolled() {
                console.log('Scrolled !')
            },
            scrollFn: function () {
                let diff = this.scrollHeight - window.pageYOffset;
                this.isBackTopFooter = diff < (this.scrollIndentBackTop - 40 - 15);
            }
        },
        components: {BackToTop}
    }

</script>
