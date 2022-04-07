import Vue from 'vue';
import VueRouter from 'vue-router';
import HomeView from '../views/HomeView.vue';
import TaskOne from '../components/TaskOne.vue';
import TaskTwo from '../components/TaskTwo.vue';
import TaskThree from '../components/TaskThree.vue';
import TaskFour from '../components/TaskFour.vue';

Vue.use(VueRouter);

const routes = [
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue'),
  },
  {
    path: '/',
    name: 'TaskOne',
    component: TaskOne,
  },
  {
    path: '/tasktwo',
    name: 'TaskTwo',
    component: TaskTwo,
  },
  {
    path: '/taskthree',
    name: 'TaskThree',
    component: TaskThree,
  },
  {
    path: '/taskfour',
    name: 'TaskFour',
    component: TaskFour,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
