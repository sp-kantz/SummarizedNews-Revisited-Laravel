<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Storage;
use Symfony\Component\Process\Exception\ProcessFailedException;
use Symfony\Component\Process\Process;
use App\Summary;
use App\Source;

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

        $process = new Process(['python', $ps.'util/backup.py']);
        $process->setTimeout(3600);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });

        //$command = escapeshellcmd('python -m scrapy.cmdline runspider '.$ps.'crawler/crawler/spiders/rss_crawler.py');
        //shell_exec($command);

        $process = Process::fromShellCommandline('python -m scrapy.cmdline runspider '.$ps.'crawler/crawler/spiders/rss_crawler.py');
        $process->setTimeout(3600);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });

        $process = new Process(['python', $ps.'clean.py']);
        $process->setTimeout(3600);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });
        
        $process = new Process(['python', $ps.'clustering.py']);
        $process->setTimeout(3600);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });

        $process = new Process(['python', $ps.'summarize.py']);
        $process->setTimeout(3600);
        $process->run(function ($type, $buffer) {
            if (Process::ERR === $type) {
                echo 'ERR > '.$buffer;
            } else {
                echo 'OUT > '.$buffer;
            }
        });

        //get json files created. store data (summaries, sources) in database
        $summaries_dir='/public/summarizer_filesystem/files/working/summaries/';
        $files=Storage::files($summaries_dir);

        foreach($files as $file){

            $data=json_decode(Storage::get($file), True);

            $summary=new Summary();
            $summary->summary_id=$data['summary_id'];
            $summary->summary_title=$data['summary_title'];
            $summary->summary_LSA=$data['summary_LSA'];
            $summary->summary_graph=$data['summary_graph'];
            $summary->save();
            
            foreach($data['summary_sources'] as $summary_source){
                
                $source=new Source();
                $source->summary_id=$data['summary_id'];
                $source->domain=$summary_source['domain'];
                $source->url=$summary_source['url'];
                $source->title=$summary_source['title'];
                $source->save();
            }
        }
        return back();
    }
}


