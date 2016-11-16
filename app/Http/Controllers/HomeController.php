<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Symfony\Component\Process\Process;
use Symfony\Component\Process\Exception\ProcessFailedException;
use App\Log;
use Auth;
use App\User;

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
    public function welcome(){
        $count = User::sum('scans');
        return view('welcome')->withCount($count);

    }
    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        $saves = Log::where('user_id',Auth::user()->id)->get();
        $count = Log::where('user_id',Auth::user()->id)->count();

        return view('home')->withSaves($saves)->withCount($count);
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
        $source = parse_url($url);
        $source = $source['host'];
        $user = Auth::user();
        $user->scans +=1;
        $user->save();
        if($save){
            $log = new Log();
            $log->url = $source;
            $log->user_id=$user->id;
            $log->output=$process->getOutput();
            $log->save();
        }

        return view('results')->withEcho($echo)->withSource($source);

    }
    public function delete($id){
              $log = Log::find($id);
              $log->delete();
              $saves = Log::where('user_id',Auth::user()->id)->get();
              $count = Log::where('user_id',Auth::user()->id)->count();

              return view('home')->withSaves($saves)->withCount($count);
    }
    public function saves($id){
        $saves = Log::findorfail($id);
        return view('saves')->withSaves($saves);
    }
}
