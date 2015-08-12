function set_cities_selected(checkbox_list){
    num = checkbox_list.find("input:checkbox[name=cities]:checked")
    $(number_cities_selected_count).text(num.length)
}

function get_city_selections(checkbox_list){

    var _checked = [];

    checkbox_list = $("#city_checkboxes_list");
    _check = checkbox_list.children();
    _check.each(function(){
        var _c = this.children; // 0 input; 1 label

        if ($(_c[0]).is(":checked")) {
            var _key = $(_c[1]).text();
            var _value = (_c[0]).value;
            var _entry = {};
            _entry[_key] = _value;
            _checked.push(_entry);
        }
    });
    return _checked;
}

function update_map(target_map){}

function loading_done(button_list, timeout){
    $("#output_loading").text("");

    setTimeout(function(){
        button_list.prop('disabled', false);
    }, timeout)
}

function output_result(result, ajax_msg, response, output_div, backend_list){

    loading_done(backend_list, 250)

    output_list = $("#output_text_list");
    output_runtime = $("#output_runtime");
    output_distance = $("#output_distance")
    output_list.empty()
    output_runtime.empty()
    output_distance.empty()

    if (ajax_msg == "success"){

        var _j = JSON.parse(response.responseText)
        var backend = _j["backend"]
        var backend_runtime = _j["backend_runtime"]
        var runtime = _j["total_runtime"]
        var backend_result = _j["result"]

        $.each(backend_result[0], function( i, v ){
            output_list.append('<li class="list-group-item">' + (i + 1) + " : " + v + '</li>');
        });

        if (runtime <= 1){
            item_status = "list-group-item-success";
        }
        else if (runtime <= 10){
            item_status = "list-group-item-warning";
        }
        else {
            item_status = "list-group-item-danger";
        }

        output_runtime.html("<li class='list-group-item " + item_status + "'>Run time: " + runtime + "s" +"</li>")
        output_distance.text("Distance: " + backend_result[1] + "km");

    } else {
        output_list.append("error connecting to backend")
    }
}

function ajax_response_wrapper(data, textStatus, jqXHR, output_div, backend_list){
    output_result(data, textStatus, jqXHR, output_div, backend_list)
}

function remove_unavailable(_this_button, _this_button_text, timeout){
    setTimeout(function(){
        _this_button.switchClass("btn-default", "btn-success")
        _this_button.text(_this_button_text)
    }, timeout)
}

function calculate_trip(backend_name, checkbox_list, backend_list, output){

    dispatch_endpoint_array = {
        "backend_python": "/api/python",
        "backend_ctypes": "/api/ctypes",
        "backend_cython": "/api/cython",
        "backend_ffi": "/api/ffi",
        "backend_python_approximation": "/api/python_approximation"
    }

    // a list of associative arrays
    // [{"new york, ny, usa":"40.734838;-73.990810"},{"portland, me, usa":"43.65...
    var city_arrays = get_city_selections(checkbox_list);
    var endpoint = dispatch_endpoint_array[backend_name];

    // shows up on second click.  fine for a demo
    $("#output_loading").html("<span class='glyphicon glyphicon-refresh glyphicon-refresh-animate'></span> loading...")

    // deactivate buttons while we're running
    backend_list.prop('disabled', true);

    // post to our given endpoint, expecting JSON in return
    var request = $.ajax({
        method: "POST",
        url: endpoint,
        dataType: 'json',
        data: {
            "json": JSON.stringify(city_arrays)
        },
        success: function(data, textStatus, jqXHR){
            ajax_response_wrapper(data, textStatus, jqXHR, output, backend_list)
        }
    })
    // this is sending the data, not the actual response from work done
    request.done()
    request.fail(function(){
        var _fake_resp = { backend: backend_name };
        var _this_button = $("#"+backend_name);
        var _this_button_text = _this_button.text();
        _this_button.switchClass("btn-success","btn-default")
        if (_this_button_text.indexOf("(unavailable)") < 0){
            _this_button.text(_this_button.text() + " (unavailable)");
        }
        ajax_response_wrapper(_fake_resp, "fail", '', output)
        loading_done(backend_list, 1000)
        remove_unavailable(_this_button, _this_button_text, 1200)
    })
}

function set_backend_handlers(checkbox_list, backend_list, output){
    // take the incoming checkbox_list array and associate handlers
    backend_list.each(function(){
        // using a var would be an error -- .each gets eval'd before
        // the .on event handler can fire, making all _id the same.
        // wouldn't be a terrible idea to disable the button to prevent "accidental" doubleclicks
        //toggle?
        $(this).on("click", function (e) {
            calculate_trip(this.id, checkbox_list, backend_list, output);
        })
    })
}

function set_checkbox_handers(checkbox_list){
    checkbox_list.children().each(function(){
        $(this).change(function(){
            set_cities_selected(checkbox_list);
        })
    })

    var _check = $("#city_checkboxes_list").children();
    var csa = $("#city_select_all")
    var csn = $("#city_select_none")

    csa.click(
        function(){
            _check.each(function(){
                var t_input = this.children[0];
                console.log(t_input)
                $(t_input).prop("checked", true); //attr("checked", "checked");
            })
        }
    )

    csn.click(
        function(){
            _check.each(function(){
                var t_input = this.children[0];
                //console.log(t_input)
                $(t_input).removeAttr('checked');
            })
        }
    )

}

function set_map(target_div, lat, long){
    var map = L.map(target_div).setView([lat, long], 13);
}

function main(){

    var checkbox_list = $("#city_checkboxes_list");
    var output = $("#output_text");
    var backend_list = $("#backend_list").find(".li_backend").children();

    set_cities_selected(checkbox_list);
    set_checkbox_handers(checkbox_list);
    set_backend_handlers(checkbox_list, backend_list, output);

}

(function(){
    console.log("<< Foreign Function Interfaces for Web Developers : github.com/tristanfisher/ffi4wd >>");
    main();
})()