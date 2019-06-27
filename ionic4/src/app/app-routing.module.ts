import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: 'login', loadChildren: './pages/login/login.module#LoginPageModule' },
  
  { path: 'owner', loadChildren: './pages/owner-tabs/owner-tabs.module#OwnerTabsPageModule' },
  { path: 'operator', loadChildren: './pages/operator-tabs/operator-tabs.module#OperatorTabsPageModule' },
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'owner-add-vehicle', loadChildren: './pages/owner-add-vehicle/owner-add-vehicle.module#OwnerAddVehiclePageModule' },
  { path: 'owner-add-operator', loadChildren: './pages/owner-add-operator/owner-add-operator.module#OwnerAddOperatorPageModule' },
  { path: 'create-company', loadChildren: './pages/create-company/create-company.module#CreateCompanyPageModule' },
  { path: 'owner-add-job', loadChildren: './pages/owner-add-job/owner-add-job.module#OwnerAddJobPageModule' },
  { path: 'owner-job-info', loadChildren: './pages/owner-job-info/owner-job-info.module#OwnerJobInfoPageModule' },
  { path: 'owner-edit-job', loadChildren: './pages/owner-edit-job/owner-edit-job.module#OwnerEditJobPageModule' },
  { path: 'owner-fleet-info', loadChildren: './pages/owner-fleet-info/owner-fleet-info.module#OwnerFleetInfoPageModule' },
  { path: 'owner-view-operator', loadChildren: './pages/owner-view-operator/owner-view-operator.module#OwnerViewOperatorPageModule' },
  { path: 'profile-details', loadChildren: './pages/profile-details/profile-details.module#ProfileDetailsPageModule' },
  { path: 'operator-job-info', loadChildren: './pages/operator-job-info/operator-job-info.module#OperatorJobInfoPageModule' },
  { path: 'operator-cap-skills', loadChildren: './pages/operator-cap-skills/operator-cap-skills.module#OperatorCapSkillsPageModule' },
  // { path: '', redirectTo: 'owner/tabs/owner-home', pathMatch: 'full' },
  // { path: 'owner-tabs', loadChildren: './pages/owner-tabs/owner-tabs.module#OwnerTabsPageModule' },
  // { path: 'owner-home', loadChildren: './pages/owner-home/owner-home.module#OwnerHomePageModule' },
  // { path: 'owner-jobs', loadChildren: './pages/owner-jobs/owner-jobs.module#OwnerJobsPageModule' },
  // { path: 'owner-fleet', loadChildren: './pages/owner-fleet/owner-fleet.module#OwnerFleetPageModule' },
  // { path: 'owner-operators', loadChildren: './pages/owner-operators/owner-operators.module#OwnerOperatorsPageModule' },
];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
