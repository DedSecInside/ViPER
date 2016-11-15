@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row" >
        <div class="col-md-12 col-md-offset-0">
            <div class="panel panel-default">
                <div class="panel-heading">Console</div>
                <div class="panel-body">
                    <h3>Please provide the url to scan!</h3>
                    <form action="/script" method="POST">
                        <label>URL:</label>
                        <input type="text" name="url">
                        <input type="hidden" name="_token" value="{{csrf_token()}}">
                        <input type="submit" class="btn btn-sm btn-primary" value="Scan">
                        <br>
                        <label>Save Output:</label>
                        <input type="checkbox" name="log" >
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
@endsection
