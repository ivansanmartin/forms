<template>
	<div class="form-metrics">
		<div class="container py-4">
			<div class="row align-items-center mb-4">
				<div class="col-md-6">
					<div class="d-flex align-items-center">
						<button class="btn btn-outline-secondary me-3">
							<i class="bi bi-arrow-left"></i> Back to All Forms
						</button>
						<div>
							<h1 class="h3 mb-0">Form Name</h1>
							<p class="text-muted mb-0">
								Form Performance Analysis
							</p>
						</div>
					</div>
				</div>
				<div class="col-md-6">
					<div class="d-flex justify-content-md-end mt-3 mt-md-0">
						<select class="form-select me-2" style="width: auto">
							<option value="last7days">Last 7 Days</option>
							<option value="last30days">Last 30 Days</option>
							<option value="last90days">Last 90 Days</option>
							<option value="custom">Custom Range</option>
						</select>
						<button class="btn btn-outline-primary me-2">
							<i class="bi bi-download"></i> Export
						</button>
						<button class="btn btn-outline-secondary">
							<i class="bi bi-gear"></i> Settings
						</button>
					</div>
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
										>↑ 10%</span
									>
								</div>
								<div
									class="bg-success bg-opacity-10 p-2 rounded"
								>
									<i
										class="bi bi-graph-up text-success fs-4"
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
						<div
							class="card-header bg-white d-flex justify-content-between align-items-center"
						>
							<h5 class="mb-0">Submission Trend</h5>
							<div>
								<button
									class="btn btn-sm btn-outline-secondary me-2"
								>
									Daily
								</button>
								<button
									class="btn btn-sm btn-outline-secondary"
								>
									Weekly
								</button>
							</div>
						</div>
						<div class="card-body" style="height: 300px"></div>
					</div>
				</div>
				<div class="col-lg-4">
					<div class="card shadow-sm h-100">
						<div class="card-header bg-white">
							<h5 class="mb-0">Completion Status</h5>
						</div>
						<div
							class="card-body d-flex flex-column justify-content-center"
						>
							<div
								style="position: relative; height: 220px"
							></div>
							<div class="text-center mt-3">
								<div class="d-flex justify-content-center">
									<div class="px-3">
										<span class="badge bg-primary"
											>68%</span
										>
										<p class="small text-muted mb-0">
											Completed
										</p>
									</div>
									<div class="px-3">
										<span class="badge bg-warning"
											>12%</span
										>
										<p class="small text-muted mb-0">
											Partial
										</p>
									</div>
									<div class="px-3">
										<span class="badge bg-danger">20%</span>
										<p class="small text-muted mb-0">
											Abandoned
										</p>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>

			<div class="row g-4">
				<div class="col-lg-6">
					<div class="card shadow-sm">
						<div class="card-header bg-white">
							<h5 class="mb-0">User Drop-off Analysis</h5>
						</div>
						<div class="card-body" style="height: 250px">
							<p class="text-muted small mt-3">
								52% of users reach the final page, with 48%
								completing submission.
							</p>
						</div>
					</div>
				</div>
				<div class="col-lg-6">
					<div class="card shadow-sm">
						<div class="card-header bg-white">
							<h5 class="mb-0">Field Error Rates</h5>
						</div>
						<div class="card-body" style="height: 250px">
							<p class="text-muted small mt-3">
								Credit Card field has the highest error rate at
								22%.
							</p>
						</div>
					</div>
				</div>
			</div>

			<div class="row mt-4">
				<div class="col-12">
					<div class="card shadow-sm">
						<div
							class="card-header bg-white d-flex justify-content-between align-items-center"
						>
							<h5 class="mb-0">Detailed Submissions</h5>
							<button class="btn btn-sm btn-outline-primary">
								Download CSV
							</button>
						</div>
						<div class="card-body p-0">
							<div class="table-responsive">
								<table class="table table-hover mb-0">
									<thead class="table-light">
										<tr>
											<th>Submission ID</th>
											<th>Date & Time</th>
											<th>User</th>
											<th>Completion Time</th>
											<th>Device</th>
											<th>Status</th>
											<th>Actions</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>#FB-1023</td>
											<td>Mar 30, 2025 09:45 AM</td>
											<td>john.doe@example.com</td>
											<td>4m 12s</td>
											<td>Desktop</td>
											<td>
												<span class="badge bg-success"
													>Complete</span
												>
											</td>
											<td>
												<button
													class="btn btn-sm btn-outline-secondary me-1"
												>
													View
												</button>
												<button
													class="btn btn-sm btn-outline-danger"
												>
													Delete
												</button>
											</td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
						<div class="card-footer bg-white text-center">
							<nav aria-label="Submissions pagination">
								<ul
									class="pagination justify-content-center mb-0"
								>
									<li class="page-item disabled">
										<a
											class="page-link"
											href="#"
											tabindex="-1"
											>Previous</a
										>
									</li>
									<li class="page-item active">
										<a class="page-link" href="#">1</a>
									</li>
									<li class="page-item">
										<a class="page-link" href="#">2</a>
									</li>
									<li class="page-item">
										<a class="page-link" href="#">3</a>
									</li>
									<li class="page-item">
										<a class="page-link" href="#">Next</a>
									</li>
								</ul>
							</nav>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>
