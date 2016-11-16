<?php

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

Route::get('/','HomeController@welcome');
Auth::routes();
Route::get('/results/{id}','HomeController@saves');
Route::post('/script','HomeController@script');
Route::post('/delete/{id}','HomeController@delete');
Route::get('/home', 'HomeController@index');
