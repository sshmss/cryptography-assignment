<template>
  <v-app dark>
    <v-app-bar
      app
      color="grey darken-4"
      dark
      elevation="0"
      height="68px"
      style="border-bottom: #3c3c3c 1px solid !important;"
    >
      <v-spacer></v-spacer>

      <v-btn
        text
      >
        <span class="mr-2">Shamis Sabah - S1901356</span>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer permanent app color="grey darken-4" class="noscroll">
      <v-list-item
      style="overflow-y: hidden !important;"
      >
        <v-list-item-content>
          <v-list-item-title class="text-h6 white--text">
            Cryptography
          </v-list-item-title>
          <v-list-item-subtitle class="white--text">
            Assignment
          </v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.to"
          link
        >
          <v-list-item-icon>
            <v-icon large color="white">{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title class="white--text title">{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <lottie-animation
          style="margin-top: 460px;"
          path="hacker-thinking-about-code.json"
        />
      </v-list>
    </v-navigation-drawer>

    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
import LottieAnimation from 'lottie-vuejs/src/LottieAnimation.vue';

export default {
  name: 'App',
  components: {
    LottieAnimation,
  },

  data: () => ({
    items: [
      { title: 'Task 1', icon: 'mdi-credit-card-check-outline', to: '/' },
      { title: 'Task 2', icon: 'mdi-code-tags-check', to: '/tasktwo' },
      { title: 'Task 3', icon: 'mdi-key-link', to: '/taskthree' },
      { title: 'Task 4', icon: 'mdi-looks', to: '/taskfour' },
    ],
    right: null,
    //
  }),
};
</script>
<style>
/* Hide scrollbar for Chrome, Safari and Opera */
.example::-webkit-scrollbar {
  display: none;
}

/* Hide scrollbar for IE, Edge and Firefox */
.example {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>
