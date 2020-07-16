<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PagesController extends Controller
{
    public function homepage(){

        return redirect('/summaries');
    }

    public function about(){

        return view('about');
    }

}
