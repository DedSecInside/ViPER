<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use App\Log;

class HomeController extends Controller
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
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        return view('home');
    }
    public function script(Request $request)
    {
        $url = $request->get('url');
        $save = $request->get('log');
        $process = new Process('cd ViPER && python3 viper.py -u '.$url);
        $process->setTimeout(3600);
        $process->run(function ($type, $buffer){
        });
        $echo = $process->getOutput();
        if($save){
            $log = new Log();
            $log->url = $url;
            $log->output=$process->getOutput();
            $log->save();
        }
        return view('results')->withEcho($echo);

    }
}
