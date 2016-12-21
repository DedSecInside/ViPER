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
        $this->middleware('auth')->except('welcome');
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
        $xss=0;
        $inj=0;
        $head=0;
        $crs=null;
        $sql=null;
        $url = $request->get('url');
        $save = $request->get('log');
        $cross = $request->get('xss');
        $sqli = $request->get('inj');
        $process = new Process('cd ViPER && python3 ViPER.py -u '.$url.' -a');
        $process->setTimeout(3600);
        $process->run(function ($type, $buffer){
        });
        $echo = $process->getOutput();
        $source = parse_url($url);
        $source = $source['host'];
        $user = Auth::user();
        $user->scans +=1;
        $user->save();
        if(strpos ($echo,'200')!=false ){
            $head=substr_count($echo, "200");
            $head = ($head/6)*100;
        }
        $xss=substr_count($echo, "Vulnerable to Clickjacking");
        $xss = ($xss/1)*100;
        $inj=substr_count($echo, "SQL Injection!");
        $inj-=4;
        $inj = ($inj/4)*100;
        if($save){
            $log = new Log();
            $log->url = $source;
            $log->user_id=$user->id;
            $log->output=$process->getOutput();
            $log->save();
        }
        if($cross){
            $process = new Process('cd ViPER && python3 ViPER.py -u '.$url.' -A3');
            $process->setTimeout(360);
            $process->run(function ($type, $buffer){
            });
            $crs = $process->getOutput();

        }
        if($sqli){
            $process = new Process('cd ViPER && python3 ViPER.py -u '.$url.' -A1');
            $process->setTimeout(360);
            $process->run(function ($type, $buffer){
            });
            $sql = $process->getOutput();

        }

        $overall=(($head+$inj+$xss)/300)*100;
        return view('results')->withEcho($echo)->withSource($source)->withXss($xss)->withInj($inj)->withHead($head)->withCrs($crs)->withSql($sql)->withOverall($overall);

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
