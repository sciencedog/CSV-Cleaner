#!/bin/env python
import csv

header = []
with open('incident.csv','r') as csvfile:
    data=csv.reader(csvfile, delimiter=',',quotechar='"')
    count = 0
    for i in data:
        for j in i:
            if j == "number":
                header.insert(count,"Number")
            elif j == "short_description":
                header.insert(count,"Subject")
            elif j == "company":
                header.insert(count,"Company")
            elif j == "caller_id":
                header.insert(count,"Submitted For")
            elif j == "priority":
                header.insert(count,"Current Priority")
            elif j == "state":
                header.insert(count,"State")
            elif j == "sys_created_on":
                header.insert(count,"Created")
            elif j == "resolved_at":
                header.insert(count,"Resolved")
            elif j == "closed_at":
                header.insert(count,"Closed")
            elif j == "assignment_group":
                header.insert(count,"Assignment Group")
            elif j == "u_acknowledged":
                header.insert(count,"Acknowledged")
            elif j == "u_acknowledgement_duration":
                header.insert(count,"Acknowledgement Duration")
            elif j == "active":
                header.insert(count,"Active")
            elif j == "activity_due":
                header.insert(count,"Activity Due")
            elif j == "u_actual_duration":
                header.insert(count,"Actual Duration")
            elif j == "u_actual_end_date":
                header.insert(count,"Actual End Date")
            elif j == "u_actual_start_date":
                header.insert(count,"Actual Start Date")
            elif j == "approval":
                header.insert(count,"Approval")
            elif j == "approval_history":
                header.insert(count,"Approval History")
            elif j == "approval_set":
                header.insert(count,"Approval Set")
            elif j == "u_asset___collection_name":
                header.insert(count,"Asset / Collection Name")
            elif j == "assigned_to":
                header.insert(count,"Assigned To")
            elif j == "u_attachment_notes":
                header.insert(count,"Attachment Note")
            elif j == "business_duration":
                header.insert(count,"Business Duration")
            elif j == "business_stc":
                header.insert(count,"Business Resolve Time")
            elif j == "u_service_impacted":
                header.insert(count,"Business Service Impacted")
            elif j == "u_campaign_name":
                header.insert(count,"Campaign Name")
            elif j == "category":
                header.insert(count,"Category")
            elif j == "caused_by":
                header.insert(count,"Caused by Change")
            elif j == "rfc":
                header.insert(count,"Change Request")
            elif j == "u_change_made_to_environment":
                header.insert(count,"Change Made to Environment Prior to Incident")
            elif j == "child_incidents":
                header.insert(count,"Child Incidents")
            elif j == "close_code":
                header.insert(count,"Close Code")
            elif j == "close_notes":
                header.insert(count,"Close Notes")
            elif j == "closed_by":
                header.insert(count,"Closed By")
            elif j == "comments":
                header.insert(count,"Comments")
            elif j == "comments_and_work_notes":
                header.insert(count,"Comments and Work Notes")
            elif j == "u_communication_interval":
                header.insert(count,"Communication Interval")
            elif j == "u_companies_affected":
                header.insert(count,"Companies Affected")
            elif j == "u_mso_types_impacted":
                header.insert(count,"Company Types Impacted")
            elif j == "cmdb_ci":
                header.insert(count,"Configuration Item")
            elif j == "contact_type":
                header.insert(count,"Contact Type")
            elif j == "correlation_id":
                header.insert(count,"Correlation ID")
            elif j == "correlation_display":
                header.insert(count,"Correlation Display")
            elif j == "knowledge":
                header.insert(count,"Create Knowledge Article")
            elif j == "sys_created_by":
                header.insert(count,"Created By")
            elif j == "impact":
                header.insert(count,"Customer / Enterprise Impact")
            elif j == "u_customer_comm_sent":
                header.insert(count,"Customer Communication Sent")
            elif j == "u_customer_updates":
                header.insert(count,"Customer Communication")
            elif j == "u_customer_comm_updates":
                header.insert(count,"Customer Communication Updates")
            elif j == "delivery_plan":
                header.insert(count,"Delivery Plan")
            elif j == "delivery_task":
                header.insert(count,"Delivery Task")
            elif j == "description":
                header.insert(count,"Description")
            elif j == "u_disposition_code":
                header.insert(count,"Disposition Code")
            elif j == "u_distribution_groups_affected":
                header.insert(count,"Distribution Groups Affected")
            elif j == "sys_domain":
                header.insert(count,"Domain")
            elif j == "u_downtime":
                header.insert(count,"Downtime")
            elif j == "due_date":
                header.insert(count,"Due Date")
            elif j == "calendar_duration":
                header.insert(count,"Duration")
            elif j == "u_email_to_case":
                header.insert(count,"Email to Case")
            elif j == "u_end_commn_sla":
                header.insert(count,"End Comm SLA")
            elif j == "u_environment_type":
                header.insert(count,"Environment Type")
            elif j == "u_escalated_to_management":
                header.insert(count,"Escalated to Management")
            elif j == "escalation":
                header.insert(count,"Escalation")
            elif j == "expected_start":
                header.insert(count,"Expected Start")
            elif j == "u_feature_type":
                header.insert(count,"Feature Type")
            elif j == "u_features":
                header.insert(count,"Features")
            elif j == "follow_up":
                header.insert(count,"Follow Up")
            elif j == "group_list":
                header.insert(count,"Group List")
            elif j == "u_has_this_incident_occurred_b":
                header.insert(count,"Has This Incident Occurred Before?")
            elif j == "u_identified_by":
                header.insert(count,"Identified By")
            elif j == "u_incident_summary":
                header.insert(count,"Incident Summary")
            elif j == "u_incident_hierarachy":
                header.insert(count,"Incident Heirarchy")
            elif j == "u_incident_manager":
                header.insert(count,"Incident Manager")
            elif j == "incident_state":
                header.insert(count,"Incident State")
            elif j == "u_include_on_availability_repo":
                header.insert(count,"Include on Availability Reporting")
            elif j == "u_initial_priority":
                header.insert(count,"Initial Priority")
            elif j == "u_justification":
                header.insert(count,"Justification")
            elif j == "u_knowledge_utilized":
                header.insert(count,"Knowledge Utilized")
            elif j == "u_hardware_platform":
                header.insert(count,"Known Devices Impacted")
            elif j == "u_last_mso_comment_time":
                header.insert(count,"Last MSO Comment Time")
            elif j == "u_last_communication_sent":
                header.insert(count,"Last Communication Sent")
            elif j == "location":
                header.insert(count,"Location")
            elif j == "u_mso_cc":
                header.insert(count,"MSO CC")
            elif j == "u_internal_reference_number":
                header.insert(count,"MSO Reference Number")
            elif j == "made_sla":
                header.insert(count,"Made SLA")
            elif j == "u_major_incident":
                header.insert(count,"Major Incident")
            elif j == "u_major_outage_summary":
                header.insert(count,"Major Outage Summary")
            elif j == "u_manual_verification_code":
                header.insert(count,"Manual Verification Code")
            elif j == "u_next_communication_due":
                header.insert(count,"Next Communication Due")
            elif j == "notify":
                header.insert(count,"Notify")
            elif j == "u_number_of_msos_impacted":
                header.insert(count,"Number of MSOs Impacted")
            elif j == "u_subscriber_complaints":
                header.insert(count,"Number of Subscriber Complaints")
            elif j == "order":
                header.insert(count,"Order")
            elif j == "u_outage_end":
                header.insert(count,"Outage End")
            elif j == "u_outage_start":
                header.insert(count,"Outage Start")
            elif j == "u_poc_name":
                header.insert(count,"POC Name")
            elif j == "u_poc_phone":
                header.insert(count,"POC Phone")
            elif j == "parent_incident":
                header.insert(count,"Parent Incident")
            elif j == "u_parent_type":
                header.insert(count,"Parent Type")
            elif j == "u_pending_expiration":
                header.insert(count,"Pending Expiration")
            elif j == "u_pending_reason":
                header.insert(count,"Pending Reason")
            elif j == "u_percent_complete":
                header.insert(count,"Percent Complete")
            elif j == "u_priority_change_count":
                header.insert(count,"Priority Change Count")
            elif j == "u_priority_changed_by":
                header.insert(count,"Priority Changed By")
            elif j == "problem_id":
                header.insert(count,"Problem")
            elif j == "u_q1":
                header.insert(count,"Q1")
            elif j == "u_q2":
                header.insert(count,"Q2")
            elif j == "u_q3":
                header.insert(count,"Q3")
            elif j == "u_reason_for_priority_change":
                header.insert(count,"Reasons for Priority Change")
            elif j == "reassignment_count":
                header.insert(count,"Reassignment Count")
            elif j == "u_region":
                header.insert(count,"Region")
            elif j == "reopen_count":
                header.insert(count,"reopen Count")
            elif j == "u_reopened_count":
                header.insert(count,"Reopened Count")
            elif j == "u_reproducability":
                header.insert(count,"Reproducability")
            elif j == "u_restoration_description":
                header.insert(count,"Resolution Description")
            elif j == "calendar_stc":
                header.insert(count,"Resolve Time")
            elif j == "resolved_by":
                header.insert(count,"Resolved By")
            elif j == "u_resolver_group":
                header.insert(count,"Resolver Group")
            elif j == "u_sf_case_number":
                header.insert(count,"SF Case Number")
            elif j == "u_issue_type":
                header.insert(count,"SLA Cancellation Reason")
            elif j == "sla_due":
                header.insert(count,"SLA Due")
            elif j == "severity":
                header.insert(count,"Severity")
            elif j == "skills":
                header.insert(count,"Skills")
            elif j == "u_software_version":
                header.insert(count,"Software Version")
            elif j == "u_source":
                header.insert(count,"Source")
            elif j == "parent":
                header.insert(count,"Source")
            elif j == "u_specific_markets_regions_vod":
                header.insert(count,"Specific Markets/Regions/VOD Sites Impacted")
            elif j == "u_start_commn_sla":
                header.insert(count,"Start Comm SLA")
            elif j == "u_step_taken_to_ruleout_issue":
                header.insert(count,"Steps Taken to Rule Out Issue")
            elif j == "u_steps_to_reproduce":
                header.insert(count,"Steps to Reproduce")
            elif j == "subcategory":
                header.insert(count,"Subcategory")
            elif j == "opened_at":
                header.insert(count,"Submitted")
            elif j == "opened_by":
                header.insert(count,"Submitted By")
            elif j == "u_tap___tsg_url":
                header.insert(count,"TAP / TSG URL")
            elif j == "u_tsns_for_the_units_affected_":
                header.insert(count,"TSNs For The Units Affected By This Issue")
            elif j == "sys_class_name":
                header.insert(count,"Task Type")
            elif j == "u_tasks_count":
                header.insert(count,"Tasks Count")
            elif j == "watch_list":
                header.insert(count,"TiVo Watchlist")
            elif j == "work_notes_list":
                header.insert(count,"TiVo Work Notes")
            elif j == "u_time_planned":
                header.insert(count,"Time Planned")
            elif j == "u_time_to_closure":
                header.insert(count,"Time to Closure")
            elif j == "u_time_to_restoration":
                header.insert(count,"Time to Restoration")
            elif j == "time_worked":
                header.insert(count,"Time Worked")
            elif j == "u_time_spent":
                header.insert(count,"Time Worked")
            elif j == "u_type":
                header.insert(count,"Type")
            elif j == "sys_updated_on":
                header.insert(count,"Updated")
            elif j == "sys_updated_by":
                header.insert(count,"Updated By")
            elif j == "sys_mod_count":
                header.insert(count,"Updates")
            elif j == "upon_approval":
                header.insert(count,"Upon Approval")
            elif j == "upon_reject":
                header.insert(count,"Upon Reject")
            elif j == "urgency":
                header.insert(count,"Urgency")
            elif j == "user_input":
                header.insert(count,"User Input")
            elif j == "u_verification_code":
                header.insert(count,"Verification Code")
            elif j == "work_end":
                header.insert(count,"Work End")
            elif j == "work_notes":
                header.insert(count,"Work Notes")
            elif j == "work_start":
                header.insert(count,"Work Start")
            elif j == "u_mso_cc_emaillist":
                header.insert(count,"MSO CC Email List")
            else:
                break
            count += 1

print "This is where the testing starts"
print "Count == %d"%count
with open('incident.csv','r') as csvfile:
    data=csv.reader(csvfile, delimiter=',',quotechar='"')
    x=0
    for i in data:
        x += 1
        if x == 1:
            continue
        count = 0
        print "\n"
        for j in i:
            if j =="":
                print "%s: Not Applicable"%header[count]
            else:
                print "%s: %s"%(header[count],j)
            count +=1
