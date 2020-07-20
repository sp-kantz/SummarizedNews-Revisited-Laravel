<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\User;
use App\Comment;

class DashboardController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        $user_id= auth()->user()->id;
        $comments=User::find($user_id)->comments()->orderBy('created_at','desc')->get();
        return view('dashboard')->with('comments', $comments);
    }
}
