@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-12 col-md-offset-0">
            <div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
                <div class="panel panel-default">
                    <div class="panel-heading" role="tab" id="heading4">
                        <h4 class="panel-title">
                            <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapse4" aria-expanded="true" aria-controls="collapse4">
                                Results
                            </a>
                        </h4>
                    </div>
                    <div id="collapse4" class="panel-collapse collapse in " role="tabpanel" aria-labelledby="heading4">
                        <div class="panel-body">
                            <h3>Overall Result</h3>
                            <div class="progress">
                            <div
                            @if($overall<=40)
                            class="progress-bar progress-bar-success"
                        @elseif($overall<=70 && $overall>40)
                            class="progress-bar progress-bar-warning"
                            @else
                            class="progress-bar progress-bar-danger"
                            @endif
                            role="progressbar" aria-valuenow="{{$overall}}" aria-valuemin="0" aria-valuemax="100" style="width: {{$overall}}%">
                                <span class="sr-only">(Vulnerable)</span>
                            </div>
                            </div>
                            <hr>
<h3>Header Checks</h3>
<div class="progress">
<div
@if($head<=40)
class="progress-bar progress-bar-success"
@elseif($head<=70 && $head>40)
class="progress-bar progress-bar-warning"
@else
class="progress-bar progress-bar-danger"
@endif
role="progressbar" aria-valuenow="{{$head}}" aria-valuemin="0" aria-valuemax="100" style="width: {{$head}}%">
    <span class="sr-only">(Vulnerable)</span>
</div>
</div>
<hr>
<h3>XSS (Cross Site Scripting Vulnerability)</h3>
<div class="progress">
<div
@if($xss<=40)
class="progress-bar progress-bar-success"
@elseif($xss<=70 && $xss>40)
class="progress-bar progress-bar-warning"
@else
class="progress-bar progress-bar-danger"
@endif
role="progressbar" aria-valuenow="{{$xss}}" aria-valuemin="0" aria-valuemax="100" style="width: {{$xss}}%">
    <span class="sr-only">(Vulnerable)</span>
</div>
</div>
<hr>
<h3>Injection Attacks</h3>
<div class="progress">
<div
@if($inj<=40)
class="progress-bar progress-bar-success"
@elseif($inj<=70 && $inj>40)
class="progress-bar progress-bar-warning"
@else
class="progress-bar progress-bar-danger"
@endif
role="progressbar" aria-valuenow="{{$inj}}" aria-valuemin="0" aria-valuemax="100" style="width: {{$inj}}%">
    <span class="sr-only">(Vulnerable)</span>
</div>
</div>
<hr>
                        </div>
                    </div>
                </div>
                @if($sql)
                <div class="panel panel-default">
                    <div class="panel-heading" role="tab" id="heading2">
                        <h4 class="panel-title">
                            <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapse2" aria-expanded="true" aria-controls="collapse2">
                                Injection Attacks
                            </a>
                        </h4>
                    </div>
                    <div id="collapse2" class="panel-collapse collapse " role="tabpanel" aria-labelledby="heading2">
                        <div class="panel-body">
                            <pre>
                                {{$sql}}
                            </pre>
                        </div>
                    </div>
                </div>
            @endif
                @if($crs)
                <div class="panel panel-default">
                    <div class="panel-heading" role="tab" id="heading3">
                        <h4 class="panel-title">
                            <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapse3" aria-expanded="true" aria-controls="collapse3">
                                XSS Raw Output
                            </a>
                        </h4>
                    </div>
                    <div id="collapse3" class="panel-collapse collapse" role="tabpanel" aria-labelledby="heading3">
                        <div class="panel-body">
                            <pre>
                                {{$crs}}
                            </pre>
                        </div>
                    </div>
                </div>
            @endif
            <div class="panel panel-default">
                <div class="panel-heading" role="tab" id="heading1">
                    <h4 class="panel-title">
                        <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapse1" aria-expanded="true" aria-controls="collapse1">
                            Raw Output of {{$source}}
                        </a>
                    </h4>
                </div>
                <div id="collapse1" class="panel-collapse collapse" role="tabpanel" aria-labelledby="heading1">
                    <div class="panel-body">
                        <pre>
                            {{$echo}}
                        </pre>
                    </div>
                </div>
            </div>
            </div>
        </div>
    </div>
</div>
@endsection
