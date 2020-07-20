<div id="sources">
    <label>Sources</label>
    <ul>
    @foreach ($sources as $source)
        <li>
            <label id="source_domain">{{$source->domain}}</label></br>
            <a href="{{$source->url}}" id="source_url">{{$source->title}}</a>
        </li>
    @endforeach
    </ul>
</div>