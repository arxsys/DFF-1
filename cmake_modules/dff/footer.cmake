function(CHECK_ORPHANED_PARENT_DEPENDENCIES target)
  set(dot_pos 0)
  set(tmp ${target})
  list(APPEND prefixes "")
  set(current_target ${target})
  while((NOT ${dot_pos} EQUAL -1) AND (NOT ${tmp} STREQUAL "dff"))
    string(FIND ${tmp} "." dot_pos REVERSE)
    string(SUBSTRING ${tmp} 0 ${dot_pos} tmp)
    list(APPEND prefixes ${tmp})
  endwhile()
  list(REVERSE prefixes)
  set(parent_target "")
  foreach(prefix ${prefixes})
    get_target_property(prop ${prefix} CREATED)
    if (NOT prop STREQUAL "true")
      log("Target <${prefix}> does not exist")
      add_custom_target("${prefix}" ALL DEPENDS ${parent_target})
      log("  custom target created with DEPENDS setted to ${parent_target}")
      set_target_properties(${prefix} PROPERTIES CREATED "true")
    endif()
    set(parent_target ${prefix})
  endforeach()
endfunction()

get_property(created_targets GLOBAL PROPERTY CREATED_TARGETS)
foreach(current_target ${created_targets})
  string(FIND ${current_target} "." dot_pos REVERSE)
  string(SUBSTRING ${current_target} 0 ${dot_pos} parent_target)
  log("Making build dependencies between ${current_target} and its parent ${parent_target}")
  if (NOT ${current_target} STREQUAL "dff")
    check_orphaned_parent_dependencies(${current_target})
    add_dependencies(${parent_target} ${current_target})
  endif()
endforeach()


log("
   ==========================================
   | .pyc files to be uninstalled with NSIS |
   ==========================================\n")
get_property(pyc_list GLOBAL PROPERTY PYC_FILES)
foreach (pyc_file ${pyc_list})
  log("${pyc_file}")
endforeach (pyc_file ${pyc_list})

include(CPack)
ENABLE_TESTING()
SUBDIRS(testsuite)
