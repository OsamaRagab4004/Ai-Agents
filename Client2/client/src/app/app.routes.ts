import { Routes } from '@angular/router';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ArticleComponent } from './article/article.component';
import { MindmapComponent } from './mindmap/mindmap.component';
import { ContentCreationHomeComponent } from './content-creation-home/content-creation-home.component';
import { TokensComponent } from './tokens/tokens.component';
import { InsertArticleComponent } from './insert-article/insert-article.component';
import { SearchComponent } from './search/search.component';
import { MilestonesComponent } from './milestones/milestones.component';
import { SmartAiComponent } from './smart-ai/smart-ai.component';

export const routes: Routes = [
    { path: 'home', component: DashboardComponent},
    { path: 'article/:articleId', component: ArticleComponent},
    { path: 'mindmap', component: MindmapComponent},
    { path: 'content-creation', component: ContentCreationHomeComponent},
    {path: 'tokens',component: TokensComponent},
    {path: 'manuel-article',component: InsertArticleComponent},
    {path: 'search',component: SearchComponent},
    {path: 'smart-ai',component: SmartAiComponent},
    {path: 'milestones',component: MilestonesComponent},
    
];
