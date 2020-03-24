#############################################################################################################################
# BWTheme 0.9.5 (https://github.com/winfuture/Bootstrap3-Webmin-Theme) - (http://theme.winfuture.it)						#
# Copyright (c) 2015 Riccardo Nobile <riccardo.nobile@winfuture.it> and Simone Cragnolini <simone.cragnolini@winfuture.it>	#
# Licensed under GPLv3 License (https://github.com/winfuture/Bootstrap3-Webmin-Theme/blob/testing/LICENSE)					#
#############################################################################################################################

BEGIN {push(@INC, "..", "lib");};

use WebminCore;
use Data::Dumper;

&ReadParse();
&init_config();

if ($in{'mod'}) {
	$minfo = { &get_module_info($in{'mod'}) };
}
else {
	$minfo = &get_goto_module();
}
$goto = $minfo ? "$minfo->{'dir'}/" :
$in{'page-container'} ? "" : "sysinfo.cgi";

if ($minfo) {
	$cat = "?$minfo->{'category'}=1";
}
if ($in{'page-container'}) {
	$goto .= "/".$in{'page-container'};
}

%text = &load_language($current_theme);
%gaccess = &get_module_acl( undef, "" );
$title = &get_html_framed_title();

do "material/lib/partial.cgi";

&header($title);
print '<nav class="navbar navbar-default navbar-webmin sticky-top navbar-expand-lg navbar-light bg-light" role="navigation">' . "\n";
	print '<button type="button" class="navbar-toggler navbar-toggle-webmin" data-toggle="collapse" data-target="#navbar-collapse">' . "\n";
		print '<span class="navbar-toggler-icon"></span>' . "\n";
	print '</button>' . "\n";

	print '<a class="navbar-brand" href="">' . &get_display_hostname() . '</a>' . "\n";
	# print '<div class="container-fluid">' . "\n";
	# 	print '<div class="navbar-header">' . "\n";

	# 	print '</div>' . "\n";
	# 	print '<div class="collapse navbar-collapse" id="navbar-collapse">' . "\n";
	# 		print '<ul class="nav navbar-nav">' . "\n";
	# 			print '<li class="visible-xs"><a data-toggle="collapse" data-target="#navbar-collapse" target="page-container" href="'. $gconfig{'webprefix'} . '/mobile_menu.cgi"><i class="fa fa-tags"></i> Main Menu</a></li>' . "\n";
	# 			%gaccess = &get_module_acl(undef, "");
	# 			if ($gconfig{'log'} && &foreign_available("webminlog")) {
	# 				print '<li><a data-toggle="collapse" data-target="#navbar-collapse" target="page-container" href="'. $gconfig{'webprefix'} . '/webminlog/"><i class="fa fa-file-text"></i> Logs</a></li>' . "\n";
	# 			}
	# 			if (&foreign_available("webmin")) {
	# 				print '<li><a data-toggle="collapse" data-target="#navbar-collapse" target="page-container" href="'. $gconfig{'webprefix'} . '/webmin/refresh_modules.cgi"><i class="fa fa-refresh"></i> Refresh</a></li>' . "\n";
	# 			}
	# 		print '</ul>' . "\n";
	# 		print '<div class="navbar-right">' . "\n";
	# 		$user = $remote_user;
	# 		if (&foreign_available("net")) {
	# 			$user = '<a data-toggle="collapse" data-target="#navbar-collapse" target="page-container" href="' . $gconfig{'webprefix'} . '/acl/edit_user.cgi?user=' . $user .'">' . $user . '</a>';
	# 		}
	# 		print '<p class="navbar-text pull-left">Welcome, ' . $user . '</p>' . "\n";
	# 		&get_miniserv_config(\%miniserv);
	# 		if ($miniserv{'logout'} && !$ENV{'SSL_USER'} && !$ENV{'LOCAL_USER'} && $ENV{'HTTP_USER_AGENT'} !~ /webmin/i) {
	# 			if ($main::session_id) {
	# 				print '<a href="'. $gconfig{'webprefix'} . '/session_login.cgi?logout=1" class="btn btn-bwtheme btn-danger navbar-btn pull-right"><i class="fa fa-sign-out"></i> Logout</a>' . "\n";
	# 			} else {
	# 				print '<a href="switch_user.cgi" class="btn btn-bwtheme btn-danger navbar-btn pull-right"> Switch user</a>' . "\n";
	# 			}
	# 		}
	# 	print '</div>' . "\n";
	# print '</div>' . "\n";
	print '<div class="collapse navbar-collapse">' . "\n";
		$user = $remote_user;
		print '<ul class="navbar-nav mr-auto"></ul>'. "\n";

		if (-r "$root_directory/webmin_search.cgi" && $gaccess{'webminsearch'}) {
			print '<form class="search-aside form-inline my-2 my-lg-0" role="search" action="webmin_search.cgi" target="page-container">' . "\n";
				print '<div class="form-group">' . "\n";
					print '<input class="form-control" name="search" placeholder="Search in ' . &get_product_name() . '" type="text">' . "\n";
				print '</div>' . "\n";
			print '</form>' . "\n";
		}

		print '<p class="navbar-text my-2 my-sm-0 mx-3">' . $user . '</p>' . "\n";
		&get_miniserv_config(\%miniserv);
		if ($miniserv{'logout'} && !$ENV{'SSL_USER'} && !$ENV{'LOCAL_USER'} && $ENV{'HTTP_USER_AGENT'} !~ /webmin/i) {
			if ($main::session_id) {
				print '<a href="'. $gconfig{'webprefix'} . '/session_login.cgi?logout=1" class="btn btn-bwtheme btn-danger navbar-btn pull-right my-0"><i class="fa fa-sign-out"></i></a>' . "\n";
			} else {
				print '<a href="switch_user.cgi" class="btn btn-bwtheme btn-danger navbar-btn pull-right"></a>' . "\n";
			}
		}

	print '</div>' . "\n";
print '</nav>' . "\n";
print '<div class="flex-fill d-flex">';
	print '<div class="col-md-2 bg-light sidebar collapse" id="navbar-collapse">';
		print '<div class="sidebar-sticky">' . "\n";
			&print_menu_opener();
			@cats = &get_visible_modules_categories();
			@modules = map { @{$_->{'modules'}} } @cats;
			foreach $cat (@cats) {
				&print_menu_category($cat->{'code'}, $cat->{'desc'});
				&print_sub_category_opener($cat->{'code'});
				foreach $module (@{$cat->{'modules'}}) {
					&print_sub_category($module->{'dir'} . '/', $module->{'desc'}, 'page-container');
				}
				&print_sub_category_closer();
			}
			&print_menu_closer();
		print '</div>';
	print '</div>';
	print '<iframe name="page-container" src="' . $goto . '" class="col-sm-10 col-12">' . "\n";
	print '</iframe>' . "\n";
print '</div>' . "\n";
