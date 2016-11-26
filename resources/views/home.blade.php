@extends('layouts.app')

@section('content')
    <style>
    .list-group-item:hover{
        border-color: #3097D1;
    }
    </style>
<div class="container">
    <div class="row" >
        <div class="col-md-12 col-md-offset-0">
            <div class="panel panel-danger">
                <div class="panel-heading">Console</div>
                <div class="panel-body">
                    <h3>Please provide the full url to scan!</h3>
                    <form action="/script" method="POST">
                        <label>URL:</label>
                        <input type="text" name="url">
                        <input type="hidden" name="_token" value="{{csrf_token()}}">
                        <input type="submit" class="btn btn-sm btn-primary" value="Scan">
                        <br>
                        <label>Save Output:</label>
                        <input type="checkbox" name="log" >
                        <label>Injection Attacks:</label>
                        <input type="checkbox" name="inj" >
                        <label>XSS:</label>
                        <input type="checkbox" name="xss" >
                    </form>
                </div>
            </div>
            <div class="panel panel-info">
                <div class="panel-heading">Recent Saved Scan Results <span class="badge"> {{$count}}</span></div>
                <div class="panel-body">
                    <div class="list-group">
                        @foreach($saves as $save)
                        <a href="{{url('results',$save->id)}}" class="list-group-item">
                            <h4 class="list-group-item-heading">www.{{$save->url}}</h4></a>
                            <form id="delete" action="{{ url('delete',$save->id)}}" method="POST">
                                <button class="btn btn-danger" type="submit">
                                Delete
                            </button>
                                {{ csrf_field() }}
                            </form>
                    @endforeach
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
