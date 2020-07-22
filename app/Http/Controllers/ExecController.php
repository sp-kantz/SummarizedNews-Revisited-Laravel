<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
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
        
        $process = new Process(['python', '/home/spyros/Summarized-News/system/summarizer_filesystem/scripts/py/clean.py']);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });
        $process = new Process(['python', '/home/spyros/Summarized-News/system/summarizer_filesystem/scripts/py/clustering.py']);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });
        return redirect('/summaries');
    }
}


