import routerAdmin from "./routes.admin";
import routerClient from "./routes.client";
import {Error404} from "../pages"
import {BasicLayout} from "../layouts"

const routes = [
    ...routerAdmin, 
    ...routerClient, 
  {
    layout: BasicLayout,
    path:"/*",
    component: Error404,
  },
];

export default routes;

