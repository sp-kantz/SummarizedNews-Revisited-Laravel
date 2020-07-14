<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class PagesController extends Controller
{
    public function homepage(){

        return view('index');
    }

    public function about(){

        return view('about');
    }

    public function summary(){

        return view('summary');
    }
}
