<template>
    <div>
        <v-card
                color="grey lighten-4"
                flat

        >
            <v-toolbar>


                <v-toolbar-title><strong class="teal--text" >Voltron</strong></v-toolbar-title>

                <v-text-field class="ml-6 mt-6"
                              @keypress.enter.prevent="searchItem"
                              v-model="model"
                              placeholder="Search"
                              outlined
                              rounded
                              solo
                              :color="'teal darken-4'"
                              :background-color="'grey lighten-5'"

                              clearable
                              flat
                              dense
                              light
                ></v-text-field>

                <NotificationBell
                        :propNotifications="notItems"

                />


                <v-menu style="border-left: 1px solid black"
                        open-on-hover
                        left
                        bottom
                >
                    <template v-slot:activator="{ on }">
                        <v-btn icon v-on="on">
                            <v-app-bar-nav-icon/>
                        </v-btn>
                    </template>

                    <v-list class="navList">
                        <v-list-item>
                            <v-list-item-avatar>
                                <v-img  src="https://cdn.vuetifyjs.com/images/lists/3.jpg"/>
                            </v-list-item-avatar>
                            <v-list-item-content>
                                <v-list-item-title>
                                    <div class="navName">Voltron Girl</div>
                                </v-list-item-title>
                            </v-list-item-content>

                        </v-list-item>

                        <v-list-item @click="()=>{this.$router.push('/home')}">
                            <v-list-item-title>Home</v-list-item-title>
                        </v-list-item>
                        <v-list-item @click="()=>{this.$router.push('/profile')}">
                            <v-list-item-title>Profile</v-list-item-title>
                        </v-list-item>
                        <v-list-item @click="()=>{this.$router.push('/feed')}">
                            <v-list-item-title>Feed</v-list-item-title>
                        </v-list-item>
                        <v-list-item @click="()=>{this.$router.push('/community')}">
                            <v-list-item-title>Communities</v-list-item-title>
                        </v-list-item>

                        <v-list-item @click="()=>{this.$router.push('/logout')}">
                            <v-list-item-title style="color: red">Log Out</v-list-item-title>
                        </v-list-item>



                    </v-list>
                </v-menu>
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
