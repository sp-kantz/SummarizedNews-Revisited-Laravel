<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', 'PagesController@homepage');
Route::get('/about', 'PagesController@about');

Route::resource('/summaries', 'SummariesController');
Auth::routes();

Route::post('/summaries/{summary_id}/comment', 'CommentsController@store');
Route::post('/dashboard/delete/{comment_id}', 'CommentsController@destroy');

Route::get('/dashboard', 'DashboardController@index');

Route::get('/exec', 'ExecController@exec');

