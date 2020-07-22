<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;


class ExecController extends Controller
{
    public function __construct()
    {
        $this->middleware('auth');
    }

    public function exec(){

        if (auth()->user()->id != 1) {
            return back()->with('error', 'Unauthorized Action');
        }

        $cp=dirname(__FILE__);
        $ps=$cp.'/../../../storage/app/public/summarizer_filesystem/scripts/py/';

        $process = new Process(['python', $ps.'clean.py']);
        
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });
        
        $process = new Process(['python', $ps.'clustering.py']);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });
        //return redirect('/summaries');
    }
}


