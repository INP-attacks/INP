The files in this folder are the files that should replace original code file of the Chromium project which we have modified.

These are the paths where the files should be put in the Chromium source code:
* ip_address.cc -> src\net\base\ip_address.cc
* cors_url_loader.cc -> src\services\network\cors\cors_url_loader.cc
* cors_url_loader_factory.h -> src\services\network\cors\cors_url_loader_factory.h
* preflight_controller.cc -> src\services\network\cors\preflight_controller.cc
* cors.cc -> src\services\network\public\cpp\cors\cors.cc
* cors.h -> src\services\network\public\cpp\cors\cors.h
* resource_request(net).cc -> src\services\network\public\cpp\resource_request.cc
* resource_request.h -> src\services\network\public\cpp\resource_request.h
* sandbox_win.cc -> src\services\service_manager\sandbox\win\sandbox_win.cc
* document.cc -> src\third_party\blink\renderer\core\dom\document.cc
* document_init.cc -> src\third_party\blink\renderer\core\dom\document_init.cc
* document_init.h -> src\third_party\blink\renderer\core\dom\document_init.h
* security_context.h -> src\third_party\blink\renderer\core\execution_context\security_context.h
* fetch_manager.cc -> src\third_party\blink\renderer\core\fetch\fetch_manager.cc
* fetch_client_settings_object_impl.cc -> src\third_party\blink\renderer\core\script\fetch_client_settings_object_impl.cc
* fetch_client_settings_object_impl.h -> src\third_party\blink\renderer\core\script\fetch_client_settings_object_impl.h
* worker_classic_script_loader.cc -> src\third_party\blink\renderer\core\workers\worker_classic_script_loader.cc
* xml_http_request.cc -> src\third_party\blink\renderer\core\xmlhttprequest\xml_http_request.cc
* event_source.cc -> src\third_party\blink\renderer\modules\eventsource\event_source.cc
* fetch_client_settings_object.h -> src\third_party\blink\renderer\platform\loader\fetch\fetch_client_settings_object.h
* fetch_client_settings_object_snapshot.h -> src\third_party\blink\renderer\platform\loader\fetch\fetch_client_settings_object_snapshot.h
* resource_fetcher.cc -> src\third_party\blink\renderer\platform\loader\fetch\resource_fetcher.cc
* resource_request(blink).cc -> src\third_party\blink\renderer\platform\loader\fetch\resource_request.cc
* network_utils.cc -> src\third_party\blink\renderer\platform\network\network_utils.cc
