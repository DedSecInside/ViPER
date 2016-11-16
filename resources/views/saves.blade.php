
@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-12 col-md-offset-0">
            <div class="panel panel-default">
                <div class="panel-heading">Showing Output of : {{$saves->url}}</div>
                <div class="panel-body" >
                    <h4>Host: {{$saves->url}}</h4>
                    <h4>Date: {{$saves->created_at}}</h4>
                <pre>
                {{$saves->output}}
                </pre>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
