import { createWebHistory, createRouter } from "vue-router";

import HomeView from "@/components/views/HomeView.vue";
import FormMetricsView from "@/components/views/FormMetricsView.vue";
import MetricsView from "@/components/views/MetricsView.vue";
import CreateFormView from "@/components/views/CreateFormView.vue";

const routes = [
    { path: "/", component: HomeView },
    { path: "/create-form", component: CreateFormView },
    { path: "/form-metrics", component: FormMetricsView },
    { path: "/metrics", component: MetricsView}

]

export const router = createRouter({
    history: createWebHistory(),
    routes
})