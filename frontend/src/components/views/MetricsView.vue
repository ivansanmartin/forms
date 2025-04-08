<template>
	<div class="metrics-dashboard">
		<div class="container py-4">
			<div class="d-flex justify-content-between align-items-center mb-4">
				<div>
					<h1 class="h3 mb-0">Form Performance Metrics</h1>
					<p class="text-muted">
						Monitor submissions and user engagement
					</p>
				</div>
				<div class="d-flex">
					<select class="form-select me-2">
						<option value="last7days">Last 7 Days</option>
						<option value="last30days">Last 30 Days</option>
						<option value="last90days">Last 90 Days</option>
						<option value="lastYear">Last Year</option>
					</select>
					<button class="btn btn-outline-primary">
						<i class="bi bi-download me-1"></i>
						Export
					</button>
				</div>
			</div>

			<div class="row g-3 mb-4">
				<div class="col-md-6 col-lg-3">
					<div class="card shadow-sm h-100">
						<div class="card-body">
							<div
								class="d-flex justify-content-between align-items-start"
							>
								<div>
									<h6 class="text-muted mb-1">
										Metric Title
									</h6>
									<h3 class="mb-0">123</h3>
									<span
										class="badge bg-success bg-opacity-10 text-success mt-2"
									>
										↑ +12%
									</span>
								</div>
								<div
									class="bg-success bg-opacity-10 p-2 rounded"
								>
									<i
										class="bi bi-bar-chart-line-fill text-success fs-4"
									></i>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="row g-4 mb-4">
				<div class="col-lg-8">
					<div class="card shadow-sm">
						<div class="card-header bg-white">
							<h5 class="mb-0">Submission Trends</h5>
						</div>
						<div class="card-body">
						</div>
					</div>
				</div>
				<div class="col-lg-4">
					<div class="card shadow-sm h-100">
						<div class="card-header bg-white">
							<h5 class="mb-0">Completion Rate</h5>
						</div>
						<div
							class="card-body d-flex justify-content-center align-items-center"
						>
							<div style="max-width: 250px">
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="row g-4">
				<div class="col-lg-6">
					<div class="card shadow-sm">
						<div class="card-header bg-white">
							<h5 class="mb-0">Field Usage</h5>
						</div>
						<div class="card-body">
						</div>
					</div>
				</div>
				<div class="col-lg-6">
					<div class="card shadow-sm">
						<div
							class="card-header bg-white d-flex justify-content-between align-items-center"
						>
							<h5 class="mb-0">Recent Submissions</h5>
							<a href="#" class="text-decoration-none"
								>View All</a
							>
						</div>
						<div class="card-body p-0">
							<div class="table-responsive">
								<table class="table table-hover mb-0">
									<thead class="table-light">
										<tr>
											<th>Date</th>
											<th>User</th>
											<th>Form</th>
											<th>Status</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>Mar 29, 2025</td>
											<td>john.doe@example.com</td>
											<td>Contact Form</td>
											<td>
												<span class="badge bg-success"
													>Complete</span
												>
											</td>
										</tr>
										<tr>
											<td>Mar 29, 2025</td>
											<td>sarah.smith@example.com</td>
											<td>Feedback Form</td>
											<td>
												<span class="badge bg-success"
													>Complete</span
												>
											</td>
										</tr>
										<tr>
											<td>Mar 28, 2025</td>
											<td>mike.jones@example.com</td>
											<td>Registration Form</td>
											<td>
												<span class="badge bg-danger"
													>Abandoned</span
												>
											</td>
										</tr>
										<tr>
											<td>Mar 28, 2025</td>
											<td>emily.parker@example.com</td>
											<td>Survey Form</td>
											<td>
												<span class="badge bg-success"
													>Complete</span
												>
											</td>
										</tr>
										<tr>
											<td>Mar 27, 2025</td>
											<td>robert.brown@example.com</td>
											<td>Application Form</td>
											<td>
												<span class="badge bg-warning"
													>Partial</span
												>
											</td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
